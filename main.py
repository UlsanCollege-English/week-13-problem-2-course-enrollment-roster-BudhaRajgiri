# main.py

def build_roster(registrations):
    """
    Build a course roster from a list of (student, course) registrations.

    Parameters
    ----------
    registrations : list of tuple(str, str)
        Each tuple contains (student_id, course_code).

    Returns
    -------
    dict
        A dictionary mapping each course_code to a sorted list of unique student_ids.
    """
    roster = {}

    for student, course in registrations:
        if course not in roster:
            roster[course] = set()
        roster[course].add(student)

    # Convert sets to sorted lists
    return {course: sorted(students) for course, students in roster.items()}


if __name__ == "__main__":
    # Example usage
    sample_registrations = [
        ("s1", "CS101"),
        ("s2", "CS101"),
        ("s1", "MATH200"),
        ("s2", "MATH200"),
        ("s1", "CS101"),  # duplicate
    ]
    roster = build_roster(sample_registrations)
    print(roster)
    # Expected output:
    # {'CS101': ['s1', 's2'], 'MATH200': ['s1', 's2']}