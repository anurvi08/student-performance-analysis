import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Anurvi", "Prachi", "Ayushi", "Priyal", "Bidanshi"],
    "Maths": [90,78,85,60,45],
    "Science": [88,70,80,65,50],
    "English":[92,75,82,58,40]
}

df = pd.DataFrame(data)
print(df)

df["Total"] = (
    df["Maths"] +
    df["Science"] +
    df["English"]
)

print(df)

df["Average"] = df["Total"]/3

print(df)

df["Status"] = df["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

print(df)

def grade(avg):

    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"
    
df["Grade"] = df["Average"].apply(grade)
print(df)

topper = df[df["Total"] == df["Total"].max()]

print("Topper:")
print(topper)

plt.bar(df["Name"], df["Average"])

plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Dashboard")

plt.show()

df.to_csv("student_report.csv", index=False)

print("Report Saved")