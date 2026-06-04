import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def pass_fail_distribution(df):

    pass_fail = df["passed"].value_counts()

    plt.figure(figsize=(6, 4))
    plt.bar(pass_fail.index, pass_fail.values)

    plt.title("1. Pass Fail Distribution")
    plt.xlabel("Passed")
    plt.ylabel("Number of Students")

    plt.show()


def attendance_vs_score(df):

    plt.figure(figsize=(10, 6))

    plt.scatter(
        df["attendance_rate"],
        df["final_score"]
    )

    plt.title("2. Attendance vs Final Score")
    plt.xlabel("Attendance Rate")
    plt.ylabel("Final Score")

    plt.show()


def study_hours_vs_score(df):

    plt.figure(figsize=(10, 6))

    plt.scatter(
        df["study_hours_per_week"],
        df["final_score"]
    )

    plt.title("3. Study Hours vs Final Score")
    plt.xlabel("Study Hours Per Week")
    plt.ylabel("Final Score")

    plt.show()


def final_score_distribution(df):

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["final_score"],
        bins=10,
        kde=True
    )

    plt.title("4. Final Score Distribution")
    plt.xlabel("Final Score")
    plt.ylabel("Number of Students")

    plt.show()


def study_hours_distribution(df):

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["study_hours_per_week"],
        bins=5,
        kde=True
    )

    plt.title("5. Study Hours Distribution")
    plt.xlabel("Study Hours Per Week")
    plt.ylabel("Number of Students")

    plt.show()


def internet_access_vs_pass_fail(df):

    tb = pd.crosstab(
        df["internet_access"],
        df["passed"]
    )

    tb.index = ["No", "Yes"]

    tb.plot(
        kind="bar",
        figsize=(8, 5)
    )

    plt.xticks(rotation=0)

    plt.title("6. Internet Access vs Pass/Fail")
    plt.xlabel("Internet Access")
    plt.ylabel("Number of Students")

    plt.legend(["Failed", "Passed"])

    plt.show()


def extracurricular_vs_pass_fail(df):

    tb2 = pd.crosstab(
        df["extracurricular"],
        df["passed"]
    )

    tb2.index = ["No", "Yes"]

    tb2.plot(
        kind="bar",
        figsize=(8, 5)
    )

    plt.xticks(rotation=0)

    plt.title("7. Extracurricular vs Pass/Fail")
    plt.xlabel("Extracurricular Activities")
    plt.ylabel("Number of Students")

    plt.legend(["Failed", "Passed"])

    plt.show()


def average_study_hours_by_gender(df):

    boys_avg = df[df["gender"] == 1]["study_hours_per_week"].mean()
    girls_avg = df[df["gender"] == 0]["study_hours_per_week"].mean()

    plt.figure(figsize=(6, 4))

    plt.bar(
        ["Boys", "Girls"],
        [boys_avg, girls_avg]
    )

    plt.title("8. Average Study Hours by Gender")
    plt.ylabel("Study Hours Per Week")

    plt.show()


def gender_vs_pass_fail(df):

    tb3 = pd.crosstab(
        df["gender"],
        df["passed"]
    )

    tb3.index = ["Female", "Male"]

    tb3.plot(
        kind="bar",
        figsize=(8, 5)
    )

    plt.xticks(rotation=0)

    plt.title("9. Gender vs Pass/Fail")
    plt.xlabel("Gender")
    plt.ylabel("Number of Students")

    plt.legend(["Failed", "Passed"])

    plt.show()


def average_study_hours_by_pass_fail(df):

    pass_avg = df[df["passed"] == "Yes"]["study_hours_per_week"].mean()
    fail_avg = df[df["passed"] == "No"]["study_hours_per_week"].mean()

    plt.figure(figsize=(6, 4))

    plt.bar(
        ["Pass", "Fail"],
        [pass_avg, fail_avg]
    )

    plt.title("10. Average Study Hours by Pass/Fail")
    plt.ylabel("Study Hours Per Week")

    plt.show()


def correlation_heatmap(df):

    corr_df = df.drop(
        ["student_id", "passed"],
        axis=1
    )

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        corr_df.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("11. Correlation Heatmap")

    plt.show()


def create_all_plots(df):

    pass_fail_distribution(df)
    attendance_vs_score(df)
    study_hours_vs_score(df)
    final_score_distribution(df)
    study_hours_distribution(df)
    internet_access_vs_pass_fail(df)
    extracurricular_vs_pass_fail(df)
    average_study_hours_by_gender(df)
    gender_vs_pass_fail(df)
    average_study_hours_by_pass_fail(df)
    correlation_heatmap(df)