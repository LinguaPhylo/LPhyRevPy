
def get_canonical(name: str):
    # case-sensitive
    greek_to_english = {
        'α': 'alpha',
        'β': 'beta',
        'γ': 'gamma',
        'δ': 'delta',
        'ε': 'epsilon',
        'ζ': 'zeta',
        'η': 'eta',
        'θ': 'theta',
        'ι': 'iota',
        'κ': 'kappa',
        'λ': 'lambda',
        'μ': 'mu',
        'ν': 'nu',
        'ξ': 'xi',
        'ο': 'omicron',
        'π': 'pi',
        'ρ': 'rho',
        'σ': 'sigma',
        'τ': 'tau',
        'υ': 'upsilon',
        'φ': 'phi',
        'χ': 'chi',
        'ψ': 'psi',
        'ω': 'omega',
        'Γ': 'Gamma',
        'Δ': 'Delta',
        'Θ': 'Theta',
        'Λ': 'Lambda',
        'Ξ': 'Xi',
        'Π': 'Pi',
        'Σ': 'Sigma',
        'Φ': 'Phi',
        'Ψ': 'Psi',
        'Ω': 'Omega',
        '∝': 'propto'
    }

    canonical_name = ''
    for char in name:
        if char in greek_to_english:
            canonical_name += greek_to_english[char]
        else:
            # Keep non-Greek characters unchanged
            canonical_name += char
    return canonical_name
