import streamlit as st
import pandas as pd
import datetime
import random
import plotly.express as px

# Company Name
st.sidebar.markdown("""
# <h1 style='font-size: 48px;'>FitFusion</h1>  
### A Smart Workout, Diet and Motivation
""", unsafe_allow_html=True)

# Sample motivational quotes
QUOTES = [
    "Push yourself, because no one else is going to do it for you.",
    "The body achieves what the mind believes.",
    "Exercise not only changes your body, it changes your mind, attitude, and mood.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Push yourself, because no one else is going to do it for you.",
    "The body achieves what the mind believes.",
    "Exercise not only changes your body, it changes your mind, attitude, and mood.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Success starts with self-discipline.",
    "Make every workout count.",
    "The only bad workout is the one that didn’t happen.",
    "Train insane or remain the same.",
    "You don’t have to be extreme, just consistent.",
    "Strive for progress, not perfection.",
    "Pain is temporary, pride is forever.",
    "Sore today, strong tomorrow.",
    "Be stronger than your excuses.",
    "It never gets easier, you just get stronger.",
    "Work hard in silence, let your success be your noise.",
    "Hustle for that muscle.",
    "Your only limit is you.",
    "Keep pushing. The pain you feel today will be the strength you feel tomorrow.",
    "Fitness is not about being better than someone else, it’s about being better than you used to be.",
    "No pain, no gain. Shut up and train.",
    "If you still look good at the end of your workout, you didn’t train hard enough.",
    "Sweat is fat crying.",
    "Wake up. Work out. Look hot. Kick ass.",
    "Fall in love with taking care of yourself.",
    "Discipline is the bridge between goals and accomplishment.",
    "You don’t find willpower, you create it.",
    "Nothing will work unless you do.",
    "A year from now, you’ll wish you had started today.",
    "When you feel like quitting, think about why you started.",
    "Small progress is still progress.",
    "A one-hour workout is 4% of your day. No excuses.",
    "Your body won’t go where your mind doesn’t push it.",
    "Winning starts with beginning.",
    "You can have results or excuses, not both.",
    "Fitness is like marriage. You can’t cheat on it and expect it to work.",
    "Excuses don’t burn calories.",
    "Strong people are harder to kill.",
    "Focus on your goal. Don’t look in any direction but ahead.",
    "Every rep counts.",
    "Champions train, losers complain.",
    "Commit to be fit.",
    "Don’t wish for it, work for it.",
    "Pain is weakness leaving the body.",
    "Sweat now, shine later.",
    "Your body can stand almost anything. It’s your mind you have to convince.",
    "Energy and persistence conquer all things.",
    "If it doesn’t challenge you, it doesn’t change you.",
    "The best project you’ll ever work on is you.",
    "Great things never come from comfort zones.",
    "Your speed doesn’t matter. Forward is forward.",
    "Make your workouts your escape.",
    "Respect your body. It’s the only one you get.",
    "If you’re tired of starting over, stop giving up.",
    "Believe in yourself and all that you are.",
    "Work hard, dream big.",
    "Train like a beast, look like a beauty.",
    "Put in the work. Results will follow.",
    "Never let success get to your head. Never let failure get to your heart.",
    "Do something today that your future self will thank you for.",
    "Effort is a choice.",
    "Wake up with determination, go to bed with satisfaction.",
    "Success is earned, not given.",
    "The only way to achieve the impossible is to believe it is possible.",
    "Get fit in the gym, lose weight in the kitchen.",
    "Motivation gets you started. Habit keeps you going.",
    "The pain you feel today will be the strength you feel tomorrow.",
    "Don't decrease the goal. Increase the effort.",
    "Don't count the days. Make the days count.",
    "Stronger every day.",
    "One more rep. One step closer.",
    "Get comfortable being uncomfortable.",
    "The gym is my therapy.",
    "Your fitness is 100% mental. Your body won’t go where your mind doesn’t push it.",
    "Every drop of sweat is a step closer to your goal.",
    "Consistency is the key to success.",
    "Your body is a reflection of your lifestyle.",
    "The best view comes after the hardest climb.",
    "Go hard or go home.",
    "Train smart, not just hard.",
    "Fitness is not a destination; it’s a way of life.",
    "The best revenge is massive success.",
    "You don’t get the body you want by sitting on the couch.",
    "Work hard, stay humble.",
    "If you want something you’ve never had, you must be willing to do something you’ve never done.",
    "Love yourself enough to live a healthy lifestyle.",
    "The only bad workout is the one you skipped.",
    "Your body hears everything your mind says. Stay positive.",
    "Lift heavy. Run fast. Stay strong.",
    "You didn’t wake up today to be mediocre.",
    "The secret of getting ahead is getting started.",
    "Stay focused and never give up.",
    "Biceps don’t grow on trees.",
    "Push past your limits.",
    "You are stronger than you think.",
    "Train harder, eat better, feel amazing.",
    "No one ever drowned in sweat.",
    "Winning is not everything, but wanting to win is.",
    "When in doubt, work out.",
    "Your health is an investment, not an expense.",
    "Keep going. Everything you need will come to you at the perfect time.",
    "Dedication, determination, discipline.",
    "Hard work beats talent when talent doesn’t work hard.",
    "The best way to predict the future is to create it.",
    "Fear is what stops you. Courage is what keeps you going.",
    "Once you see results, it becomes an addiction.",
    "Don't compare yourself to others. Compare yourself to the person from yesterday.",
    "One day or day one. You decide.",
    "Stronger than your excuses.",
]

def get_random_quote():
    return random.choice(QUOTES)

# Load workout and diet suggestion data
workout_data = pd.read_csv("datasets\workout_recommendations.csv")
diet_data = pd.read_csv("datasets\diet_recommendations.csv")

# App Title
st.title("🏋️‍♂️ Fitness Tracking Dashboard")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Progress", "Suggest Workout & Diet", "Workout Tracker", "Diet Tracker",  "Motivation"])

# Progress Tracking

if page == "Progress":
    
    st.header("Fitness Progress")
    weight = st.number_input("Current Weight (kg)", min_value=30.0)
    height = st.number_input("Height (cm)", min_value=100.0)
    goal_weight = st.number_input("Goal Weight (kg)", min_value=30.0)
    
    bmi = weight / ((height / 100) ** 2)
    st.metric("Your BMI", round(bmi, 2))
    
    progress_log = st.file_uploader("Upload your progress log (CSV)", type=["csv"])
    if progress_log:
        df_progress = pd.read_csv(progress_log)
        st.write("### Progress Log", df_progress)
        st.plotly_chart(px.line(df_progress, x="Date", y="Weight", title="Weight Progress"))


# Suggest Workout & Diet

elif page == "Suggest Workout & Diet":
    st.header("Personalized Workout & Diet Plan")
    age = st.number_input("Age", min_value=10, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    height = st.number_input("Height (cm)", min_value=100.0)
    weight = st.number_input("Weight (kg)", min_value=30.0)
    goal = st.selectbox("Workout Goal", ["Weight Loss", "Muscle Gain", "Endurance", "General Fitness"])
    
    if st.button("Get Suggestions"):
        suggested_workout = workout_data[workout_data["Goal"] == goal].sample(1)
        suggested_diet = diet_data[diet_data["Goal"] == goal].sample(1)
        
        st.subheader("Suggested Workout Plan")
        st.write(suggested_workout)
        
        st.subheader("Suggested Diet Plan")
        st.write(suggested_diet)
  

# Workout Tracker

elif page == "Workout Tracker":
    
    st.header("Workout Tracking")
    steps = st.number_input("Daily Steps Count", min_value=0)
    total_time = st.number_input("Total Workout Time (mins)", min_value=0)
    calories_burned = st.number_input("Calories Burned", min_value=0)
    
    st.metric("Steps Count", steps)
    st.metric("Total Workout Time", total_time)
    st.metric("Calories Burned", calories_burned)
    
    workout_log = st.file_uploader("Upload your workout log (CSV)", type=["csv"])
    if workout_log:
        df_workout = pd.read_csv(workout_log)
        st.write("### Workout Log", df_workout)
        st.plotly_chart(px.line(df_workout, x="Date", y="Calories Burned", title="Calories Burned Over Time"))

# Diet Tracker

elif page == "Diet Tracker":
    st.header("Diet Tracking")
    diet_log = st.file_uploader("Upload your diet log (CSV)", type=["csv"])
    
    if diet_log:
        df_diet = pd.read_csv(diet_log)
        st.write("### Diet Log", df_diet)
        st.plotly_chart(px.pie(df_diet, values='Calories', names='Food', title='Caloric Breakdown'))

# Motivation
elif page == "Motivation":
    st.header("Daily Motivation")
    st.subheader(get_random_quote())
