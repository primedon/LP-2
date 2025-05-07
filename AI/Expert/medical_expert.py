def recommend_department(symptom):
    if symptom == "fever":
        return "Visit General Medicine."
    elif symptom == "pain":
        return "Visit Orthopedics or Pain Management."
    elif symptom == "injury":
        return "Visit Emergency or Trauma Care."
    elif symptom == "anxiety":
        return "Visit Psychiatry or Counseling."
    else:
        return "Consult Reception for further help."

# --- Example Usage ---
symptom = input("Enter main symptom (fever/pain/injury/anxiety): ").lower()
print(recommend_department(symptom))