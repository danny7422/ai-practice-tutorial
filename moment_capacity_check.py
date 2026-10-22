def check_beam_flexure(section_name, l_b, l_p, z_x, f_y, compact=True):
    """
    Check if the beam is in zone 1 and calculate its LRFD moment capacity.
    Return a dictionary of calculated values if acceptable, or None if unacceptable.
    """
    print(f"\nChecking Section: {section_name}")

    # 1. Check compactness
    if not compact:
        print("Result: Unacceptable. Beam must be compact.")
        return None


result = check_beam_flexure("W14x90", l_b=15.0, l_p=15.2, z_x=157.0, f_y=50.0, compact=False)
print(result)