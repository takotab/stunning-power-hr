from vu_test_power_profile import Person

if __name__ == "__main__":
    froome = Person(375, 20250)
    current_p = 150
    done = True
    while done:
        done = froome.cycle(current_p, 60)
        current_p += 25
        if current_p > 900:
            break
