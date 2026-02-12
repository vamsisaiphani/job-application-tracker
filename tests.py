from main import read_applications, write_applications, VALID_STATUSES

def test_valid_statuses():
    assert "Applied" in VALID_STATUSES
    assert "Interview" in VALID_STATUSES
    assert "Rejected" in VALID_STATUSES

def test_write_and_read():
    sample_data = [
        "TestCompany,TestRole,2026-01-01,Applied,Test note\n"
    ]

    write_applications(sample_data)
    data = read_applications()

    assert len(data) == 1
    assert "TestCompany" in data[0]

if __name__ == "__main__":
    test_valid_statuses()
    test_write_and_read()
    print("✅ All tests passed")
