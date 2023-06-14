import pandas as pd
import streamlit as st

# Load the diabetes dataset
diabetes = pd.read_csv('diabetes cleaned 14.csv')

# Section 1: Picture
st.title("Diabetes")
st.header("Section 1: Picture")

# Section 2: Introduction
st.header("Section 2: Introduction")
st.write("Diabetes is a chronic metabolic disorder characterized by high blood sugar levels over a prolonged period. It occurs when the body either does not produce enough insulin or does not effectively use the insulin it produces. Insulin is a hormone that regulates blood sugar levels and allows glucose to enter cells to be used as energy.")

# Section 3: Visualization
st.header("Section 3: Visualization")

# Visualize the distribution of age
st.subheader("Age Distribution")
st.hist_chart(diabetes['Age'], bins='auto')

# Visualize the distribution of BMI
st.subheader("BMI Distribution")
st.hist_chart(diabetes['BMI'], bins='auto')

# Visualize the distribution of number of times pregnant
st.subheader("Number of Times Pregnant Distribution")
st.hist_chart(diabetes['Number of times pregnant'], bins='auto')
# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "Smoking" and "Diabetic"
st.subheader("Relationship between Smoking and Diabetic")
sns.countplot(x='Smoking', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Smoking and Diabetic')
plt.xlabel('Smoking')
plt.ylabel('Count')

# Display the plot
st.pyplot()
# Section 3: Visualization
st.header("Section 3: Visualization")

# Calculate the count of each category in the "Smoking" column
smoking_counts = diabetes['Smoking'].value_counts()

# Create a pie chart to visualize the distribution
st.subheader("Distribution of Smoking Status")
fig, ax = plt.subplots()
ax.pie(smoking_counts, labels=smoking_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title("Distribution of Smoking Status")
st.pyplot(fig)

# Create a countplot to visualize the relationship between "Smoking" and "Diabetic"
st.subheader("Relationship between Smoking and Diabetic")
sns.countplot(x='Smoking', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Smoking and Diabetic')
plt.xlabel('Smoking')
plt.ylabel('Count')

# Display the plot
st.pyplot()

# Section 3: Visualization
st.header("Section 3: Visualization")

# Calculate the count of each category in the "Alcohol" column
alcohol_counts = diabetes['Alcohol'].value_counts()

# Create a pie chart to visualize the distribution
st.subheader("Distribution of Alcohol Consumption")
fig, ax = plt.subplots()
ax.pie(alcohol_counts, labels=alcohol_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title("Distribution of Alcohol Consumption")
st.pyplot(fig)

# Create a countplot to visualize the relationship between "Alcohol" and "Diabetic"
st.subheader("Relationship between Alcohol Consumption and Diabetic")
sns.countplot(x='Alcohol', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Alcohol Consumption and Diabetic')
plt.xlabel('Alcohol')
plt.ylabel('Count')

# Display the plot
st.pyplot()

# Calculate the count of each category in the "stress" column
stress_counts = diabetes['Stress'].value_counts()

# Create a pie chart to visualize the distribution
st.subheader("Distribution of Stress")
fig, ax = plt.subplots()
ax.pie(stress_counts, labels=stress_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title("Distribution of Stress")
st.pyplot(fig)

# Create a countplot to visualize the relationship between "stress" and "Diabetic"
st.subheader("Relationship between Stress and Diabetic")
sns.countplot(x='Stress', hue='Diabetic', data=diabetes,
              order=['Not at all', 'Sometimes', 'Often', 'Very often', 'Always'])

# Set the plot title and labels
plt.title('Relationship between Stress and Diabetic')
plt.xlabel('Stress')
plt.ylabel('Count')

# Display the plot
st.pyplot()

# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "Gender" and "Diabetic"
st.subheader("Relationship between Gender and Diabetic")
sns.countplot(x='Gender', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Gender and Diabetic')
plt.xlabel('Gender')
plt.ylabel('Count')

# Display the plot
st.pyplot()
# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "Family_Diabetes" and "Diabetic"
st.subheader("Relationship between Family Diabetes and Diabetic")
sns.countplot(x='Family_Diabetes', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Family Diabetes and Diabetic')
plt.xlabel('Family Diabetes')
plt.ylabel('Count')

# Display the plot
st.pyplot()

# Section 3: Visualization
st.header("Section 3: Visualization")


# Create a countplot to visualize the relationship between "RegularMedicine" and "Diabetic"
st.subheader("Relationship between Regular Medicine and Diabetic")
ax = sns.countplot(x='RegularMedicine', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Regular Medicine and Diabetic')
plt.xlabel('Regular Medicine')
plt.ylabel('Count')

# Add legend
legend_labels = ['Does Not Take Medicine', 'Takes Medicine']
ax.legend(title='Diabetic', labels=legend_labels)

# Display the plot
st.pyplot()

# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "JunkFood" and "Diabetic"
st.subheader("Relationship between Junk Food and Diabetic")
sns.countplot(x='JunkFood', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Junk Food and Diabetic')
plt.xlabel('Junk Food')
plt.ylabel('Count')

# Add legend
plt.legend(title='Diabetic')

# Display the plot
st.pyplot()
# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "Blood Pressure level" and "Diabetic"
st.subheader("Relationship between Blood Pressure Level and Diabetic")
sns.countplot(x='BloodPressure level', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Blood Pressure Level and Diabetic')
plt.xlabel('Blood Pressure Level')
plt.ylabel('Count')

# Add legend
plt.legend(title='Diabetic')

# Display the plot
st.pyplot()
st.header("Section 3: Visualization")

# Visualize the relationship between BMI and Diabetic using a box plot
st.subheader("BMI vs Diabetic (Box Plot)")
fig, ax = plt.subplots()
sns.boxplot(x='Diabetic', y='BMI', data=diabetes)
plt.xlabel("Diabetic")
plt.ylabel("BMI")
st.pyplot(fig)

# Visualize the relationship between BMI and Diabetic using a violin plot
st.subheader("BMI vs Diabetic (Violin Plot)")
fig, ax = plt.subplots()
sns.violinplot(x='Diabetic', y='BMI', data=diabetes)
plt.xlabel("Diabetic")
plt.ylabel("BMI")
st.pyplot(fig)
# Section 3: Visualization
# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a box plot to visualize the relationship between "Age" and "Diabetic"
st.subheader("Relationship between Age and Diabetic")
sns.boxplot(x='Diabetic', y='Age', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Age and Diabetic')
plt.xlabel('Diabetic')
plt.ylabel('Age')

# Display the plot
st.pyplot()

# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "PhysicallyActive" and "Diabetic"
st.subheader("Relationship between Physically Active and Diabetic")
sns.countplot(x='PhysicallyActive', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Physically Active and Diabetic')
plt.xlabel('Physically Active')
plt.ylabel('Count')

# Add legend
plt.legend(title='Diabetic')

# Display the plot
st.pyplot()
# Violin plot to visualize the relationship between "Sleeping hours" and "Diabetic"
st.subheader("Relationship between Sleeping Hours and Diabetic (Violin Plot)")
sns.violinplot(x='Diabetic', y='Sleeping hours', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Sleeping Hours and Diabetic')
plt.xlabel('Diabetic')
plt.ylabel('Sleeping Hours')

# Display the plot
st.pyplot()
# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "Age" and "Diabetic"
st.subheader("Relationship between Age and Diabetic")
sns.countplot(x='Age', hue='Diabetic', data=diabetes, order=['A', 'B', 'C', 'D'])

# Set the plot title and labels
plt.title('Relationship between Age and Diabetic')
plt.xlabel('Age')
plt.ylabel('Count')

# Display the plot
st.pyplot()
# Create a countplot to visualize the relationship between "Age" and "Diabetic"
st.subheader("Relationship between Age and Diabetic")
age_ranges = {'A': '0-40', 'B': '50-59', 'C': '40-49', 'D': '60-99'}
diabetes['Age Range'] = diabetes['Age'].map(age_ranges)
sns.countplot(x='Age Range', hue='Diabetic', data=diabetes, order=['0-40', '50-59', '40-49', '60-99'])

# Set the plot title and labels
plt.title('Relationship between Age and Diabetic')
plt.xlabel('Age Range')
plt.ylabel('Count')

# Add legend
legend_labels = ['Does  Have Diabetes', 'Does not Have Diabetes']
plt.legend(title='Diabetic', labels=legend_labels)

# Display the plot
st.pyplot()
# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "Number of times pregnant" and "diabetic"
st.subheader("Relationship between Number of Times Pregnant and Diabetic")
sns.countplot(x='Number of times pregnant', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Number of Times Pregnant and Diabetic')
plt.xlabel('Number of Times Pregnant')
plt.ylabel('Count')

# Display the plot
st.pyplot()
# Section 3: Visualization
st.header("Section 3: Visualization")

# Add a sidebar checkbox for selecting the hue variable
hue_variable = st.sidebar.selectbox("Select Hue Variable", ['Diabetic', 'Gender'])

# Create a countplot to visualize the relationship between "Family_Diabetes" and the selected hue variable
st.subheader("Relationship between Family Diabetes and {}".format(hue_variable))
fig, ax = plt.subplots()
sns.countplot(x='Family_Diabetes', hue=hue_variable, data=diabetes)
plt.title('Relationship between Family Diabetes and {}'.format(hue_variable))
plt.xlabel('Family Diabetes')
plt.ylabel('Count')
plt.legend(title=hue_variable)
st.pyplot(fig)
# Section 3: Visualization
st.header("Section 3: Visualization")

# Add a selectbox to choose the visualization technique
visualization_type = st.selectbox("Select Visualization Type", ['Bar Plot', 'Pie Chart'])

if visualization_type == 'Bar Plot':
    # Create a bar plot to visualize the relationship between "Family_Diabetes" and "Diabetic"
    st.subheader("Relationship between Family Diabetes and Diabetic")
    sns.countplot(x='Family_Diabetes', hue='Diabetic', data=diabetes)
    plt.title('Relationship between Family Diabetes and Diabetic')
    plt.xlabel('Family Diabetes')
    plt.ylabel('Count')
    st.pyplot()

elif visualization_type == 'Pie Chart':
    # Calculate the count of each category in the "Family_Diabetes" column
    family_diabetes_counts = diabetes['Family_Diabetes'].value_counts()

    # Create a pie chart to visualize the distribution
    st.subheader("Distribution of Family Diabetes")
    fig, ax = plt.subplots()
    ax.pie(family_diabetes_counts, labels=family_diabetes_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title("Distribution of Family Diabetes")
    st.pyplot(fig)
# Section 3: Visualization
st.header("Section 3: Visualization")

# Add sliders to select the range of sleeping hours
sleeping_hours_min = st.slider("Minimum Sleeping Hours", min_value=0, max_value=12, value=0)
sleeping_hours_max = st.slider("Maximum Sleeping Hours", min_value=0, max_value=12, value=12)

# Filter the dataset based on selected sleeping hours range
filtered_data = diabetes[(diabetes['Sleeping hours'] >= sleeping_hours_min) & (diabetes['Sleeping hours'] <= sleeping_hours_max)]

# Violin plot to visualize the relationship between "Sleeping hours" and "Diabetic"
st.subheader("Relationship between Sleeping Hours and Diabetic (Violin Plot)")
sns.violinplot(x='Diabetic', y='Sleeping hours', data=filtered_data)

# Set the plot title and labels
plt.title('Relationship between Sleeping Hours and Diabetic')
plt.xlabel('Diabetic')
plt.ylabel('Sleeping Hours')

# Display the plot
st.pyplot()
# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a scatter plot to visualize the relationship between "BMI" and "Diabetic"
st.subheader("BMI vs Diabetic (Scatter Plot)")

# Create a slider to adjust the marker size based on BMI
marker_size = st.slider("Marker Size", min_value=5, max_value=15, value=10, step=1)

# Filter the data to include only diabetic patients
diabetic_data = diabetes[diabetes['Diabetic'] == True]

# Scatter plot with marker size based on BMI
sns.scatterplot(x='Diabetic', y='BMI', data=diabetic_data, s=marker_size)

# Set the plot title and labels
plt.xlabel("Diabetic")
plt.ylabel("BMI")

# Display the plot
st.pyplot()

# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "PhysicallyActive" and "Diabetic"
st.subheader("Relationship between Physically Active and Diabetic")

# Add an interactive dropdown for the PhysicallyActive column
physically_active_options = ['less than 30 min', 'more than 30 min', '1 hour or more']
selected_physically_active = st.selectbox("Select Physically Active", physically_active_options)

# Filter the data based on the selected PhysicallyActive option
filtered_data = diabetes[diabetes['PhysicallyActive'] == selected_physically_active]

# Create the countplot using the filtered data
fig, ax = plt.subplots()
sns.countplot(x='PhysicallyActive', hue='Diabetic', data=filtered_data)

# Set the plot title and labels
plt.title('Relationship between Physically Active and Diabetic')
plt.xlabel('Physically Active')
plt.ylabel('Count')

# Display the plot
st.pyplot(fig)
