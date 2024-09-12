import pandas as pd
import matplotlib.pyplot as plt

def main():

    temp_df = pd.read_excel('Module1_Dataset.xlsx')
    # print(temp_df)
    
    # What are the different kinds of indicators
    column_name = temp_df.value_counts('Indicator')
    print(column_name)
    
    # What are the top 5 states that has the maximum number of different indicators
    anxiety_df = temp_df[temp_df['Indicator'] == 'Symptoms of Anxiety Disorder']
    depression_df = temp_df[temp_df['Indicator'] == 'Symptoms of Depressive Disorder']
    anxiety_depress_df = temp_df[temp_df['Indicator'] == 'Symptoms of Anxiety Disorder or Depressive Disorder']
    state_anxiety = anxiety_df['State'].value_counts()
    state_depress = depression_df['State'].value_counts()
    state_axiety_dep = anxiety_depress_df['State'].value_counts()
    print("\nTop 5 States with Anxiety: \n",state_anxiety.head(5), "\nTop 5 States with Depression: \n",state_depress.head(5), "\nTop 5 States with Anxiety or Depression: \n", state_axiety_dep.head(5))
    
    # What are the top 5 states that has the minimum number of different indicators
    print("\nTop 5 States with minimum Anxiety: \n",state_anxiety.tail(5), "\nTop 5 States with Depression: \n",state_depress.tail(5), "\nTop 5 States with Anxiety or Depression: \n", state_axiety_dep.tail(5))
    
    # What is the top state with highest average percentage with Anxiety, Depression, Anxiety or Depression
    avg_anxiety = anxiety_df.groupby('State')['Value'].mean()
    avg_depression = depression_df.groupby('State')['Value'].mean()
    avg_anxiety_dep = anxiety_depress_df.groupby('State')['Value'].mean()
    print("\nTop state with the highest average anxiety value: \n",avg_anxiety.head(1), "\nTop state with highest average depression value: \n",avg_depression.head(1), "\nTop state with the highest average of either anxiety or depressions: \n", avg_anxiety_dep.head(1))

    # What is the top state with the least average percentage with Anxiety, Depression, Anxiety or Depression
    print("\nTop state with the least average anxiety value: \n",avg_anxiety.tail(1), "\nTop state with least average depression value: \n",avg_depression.tail(1), "\nTop state with the least average of either anxiety or depressions: \n", avg_anxiety_dep.tail(1))

    # Which time frame reported the highest symptoms (by state)
    tf_anxiety = anxiety_df.groupby(['State', 'Time Period Label'])['Value'].max()
    tf_depression = depression_df.groupby(['State', 'Time Period Label'])['Value'].max()
    tf_anxiety_dep = anxiety_depress_df.groupby(['State', 'Time Period Label'])['Value'].max()
    print("\nTime frame with highest anxiety: \n", tf_anxiety, "\nTime frame with highest depression: \n",tf_depression, "\nTime frame with highest anxiety or depression: \n",tf_anxiety_dep)
    
    # Visualization of anxiety and depression percentages
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

    # Anxiety values
    avg_anxiety.plot(kind='barh', ax=ax[0], color='skyblue')
    ax[0].set_title('Average Anxiety Symptoms by State')
    ax[0].set_xlabel('Average Percentage')

    # Depression values
    avg_depression.plot(kind='barh', ax=ax[1], color='salmon')
    ax[1].set_title('Average Depression Symptoms by State')
    ax[1].set_xlabel('Average Percentage')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()