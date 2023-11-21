import csv
import logging
import os
import re
from typing import List, Optional, Dict

from lphy.base.evolution.alignment.Alignment import Alignment
from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Value import Value

AGE_DIRECTION = "ageDirection"
AGE_REGEX = "ageRegex"
SPECIES_REGEX = "speciesRegex"


# AGE_DIRECTION, AGE_REGEX, SPECIES_REGEX
def get_option_value(options_val: Value, option_key=AGE_REGEX):
    if options_val:
        options: Dict = options_val.value  # value() is reserved by python
        v = options.get(option_key)  # return None if key doesn't exist
        if isinstance(v, Value):
            return v.value
        else:
            return v
    else:
        return None


def parse_date_string(dates_str):
    vals = []
    for date_str in dates_str:
        try:
            vals.append(float(date_str))
        except ValueError:
            # The value is not numeric, assume it is a date in the format 'uuuu-MM-dd'
            logging.warning(f"Warning: the value ({date_str}) is not numeric, "
                            f"so guess it is a date by uuuu-MM-dd format")
            return []
    return vals


# def parse_date_string(date_str: str) -> Optional[float]:
#     try:
#         date = datetime.strptime(date_str, "%Y-%m-%d")
#         return float(date.year)
#     except ValueError:
#         return None


def convert_date_to_age(dates: List[str], chrono_unit: Optional[str]) -> List[float]:
    # TODO: Implement date to age conversion
    pass


def get_first_match(taxon_name, age_regx_str):
    # guess dates
    regx = re.compile(age_regx_str)
    result = regx.search(taxon_name)
    if result:
        return result.group(1)
    raise ValueError(f"Cannot extract attributes from {taxon_name} using {regx}")


# used to be set_ages_parsed_from_taxa_name
def get_ages_map_from_taxa(alignment: Alignment, age_regx_str) -> Dict:
    age_string_map = {}

    for taxon_name in alignment.get_taxa_names():
        # TODO take nth element given separator
        age_string_map[taxon_name] = get_first_match(taxon_name, age_regx_str)

    if len(age_string_map) != alignment.n_taxa():
        raise RuntimeError(f"After parsing ages from taxa name, expect the size not changed. "
                           f"But map ({len(age_string_map)}) != n_taxa ({alignment.n_taxa()})")

    return age_string_map


class ReadOptions:

    def __init__(self, file: Value, options: Value):
        self.file = file
        self.options = options

        self.age_direction = get_option_value(self.options, AGE_DIRECTION)
        self.age_regx = get_option_value(self.options, AGE_REGEX)
        self.species_regx = get_option_value(self.options, SPECIES_REGEX)

        if self.age_direction is None and self.age_regx is None and self.species_regx is None:
            raise ValueError(f"Invalid options, cannot parse age direction, age regex, "
                             f"and species regex : {self.options}")

    def write_ages_to_file(self, alignment: Alignment):
        age_string_map = get_ages_map_from_taxa(alignment, self.age_regx)
        # only available for years
        ages_dict = AgeDirection.get_ages_dict(age_string_map, self.age_direction, alignment)

        # write ages to file
        file_name = self.get_ages_file_name()

        with open(file_name, 'w') as f:
            w = csv.writer(f, delimiter='\t')
            w.writerow(["taxon", "age"]) # header
            for key, value in sorted(ages_dict.items()):
                the_row = [key, value]  # Create the row with key and value
                w.writerow(the_row)  # Write the full row
        logging.info(f"Write the taxa ages into a file {file_name}.")

    def get_ages_file_name(self):
        base_name, _ = os.path.splitext(self.file.value)
        return base_name + "-taxa-ages.tsv"


class AgeDirection:
    # age directions
    FORWARD = "forward"  # virus , default
    BACKWARD = "backward"  # fossils
    DATES = "dates"  # forward
    AGES = "ages"  # backward

    # used to call assign_ages
    @classmethod
    def get_ages_dict(cls, age_string_map: dict, age_direction_str: str, alignment: Alignment, chrono_unit="years"):
        """
        :param age_string_map:  get from get_age_direction
        :param age_direction_str:  age direction
        :param alignment:       Alignment
        :param chrono_unit:     time unit
        :return:  a dict to map taxon name to age
        """
        age_direction = cls.get_age_direction(age_direction_str)

        # String processing
        dates_str = age_string_map.values()
        vals = parse_date_string(dates_str)

        if vals is None:
            raise UnsupportedOperationException("Date is unsupported at the moment !")
            # TODO
            vals = convert_date_to_age(dates_str, chrono_unit)

        max_age = max(vals)
        min_age = min(vals)

        # Assign ages
        taxa_names = list(age_string_map.keys())
        if len(age_string_map) != alignment.n_taxa():
            raise ValueError(f"Invalid ages/dates map: size ({len(age_string_map)}) != taxa ({len(alignment.taxa)}) !")

        ages_dict = {}

        for i, taxon_name in enumerate(taxa_names):
            index_of_taxon = alignment.index_of_taxon(taxon_name)
            if index_of_taxon < 0:
                raise RuntimeError(f"Cannot locate taxon name {taxon_name} in taxa {alignment.get_taxa_names()}")

            if age_direction in [cls.FORWARD, cls.DATES]:
                #alignment.taxa[index_of_taxon].set_age(max_age - vals[i])  # TODO rm?
                ages_dict[taxon_name] = max_age - vals[i]
            elif age_direction in [cls.BACKWARD, cls.AGES]:
                #alignment.taxa[index_of_taxon].set_age(vals[i] - min_age)  # TODO rm?
                ages_dict[taxon_name] = vals[i] - min_age
            else:
                raise ValueError(f"Not recognized age direction to convert dates or ages: {age_direction}")

        return ages_dict

    @classmethod
    def get_age_direction(cls, age_direction_str=FORWARD):
        lower_case = age_direction_str.lower()
        if lower_case not in [cls.FORWARD, cls.BACKWARD, cls.DATES, cls.AGES]:
            raise ValueError(f"Invalid age direction string {age_direction_str} !")
        return lower_case


# TODO
class Species:
    def set_species_parsed_from_taxa_name(sp_regx_str):
        self.sp_regx_str = sp_regx_str

        # guess species
        regx = re.compile(sp_regx_str)

        for taxon in self.get_taxon_array():
            taxon_name = taxon.get_name()
            sp_str = self.get_first_match(taxon_name, regx)
            taxon.set_species(sp_str)

