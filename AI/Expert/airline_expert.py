def recommend_schedule(time_of_day, cargo_type):
    if time_of_day == "morning" and cargo_type == "passenger":
        return "Schedule high-frequency short-haul flights."
    elif time_of_day == "night" and cargo_type == "cargo":
        return "Schedule overnight long-haul cargo flights."
    elif time_of_day == "evening" and cargo_type == "passenger":
        return "Allocate medium-haul routes for business travelers."
    elif cargo_type == "express":
        return "Prioritize immediate delivery routes."
    else:
        return "Use flexible scheduling based on demand."

# --- Example Usage ---
time_of_day = input("Enter time of day (morning/evening/night): ").lower()
cargo_type = input("Enter cargo type (passenger/cargo/express): ").lower()
print(recommend_schedule(time_of_day, cargo_type))
