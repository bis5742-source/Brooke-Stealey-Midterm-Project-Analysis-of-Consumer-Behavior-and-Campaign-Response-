# Brooke-Stealey-Midterm-Project-
Exploring how consumer behavior relates to marketing campaign response using Python-based EDA and an interactive Streamlit application.

# Consumer Behavior and Campaign Response: A Behavioral Analysis

## Introduction

For this project, I wanted to explore how different types of customer behavior relate to whether someone responds to a marketing campaign. While many analyses focus on identifying which customers spend the most, I was more interested in understanding why certain customers engage with marketing efforts and others do not. Because I am interested in psychology, I approached this project from a behavioral perspective rather than just a financial one.

Instead of only looking at totals or averages, I focused on how patterns such as browsing, purchasing, and deal-seeking behavior might reflect different decision-making tendencies. My goal was to better understand what separates active, engaged customers from those who are less responsive, and how businesses might use this information to improve their marketing strategies.

## Dataset Overview

This project uses a retail customer dataset containing information on 2,240 individuals, with each row representing a single customer. 

The dataset includes a wide range of variables, such as:
Demographics (age, education, marital status)
Household structure (number of children)
Income
Spending across different product categories (wine, meat, fruits, etc.)
Purchasing behavior across channels (web, store, catalog)
Website activity
Campaign response (whether the customer responded to the most recent campaign)

One limitation of the dataset is that it does not specify the exact nature of the campaign itself. Because of this, the analysis focuses on general patterns of engagement rather than responses to a specific type of marketing strategy.

## Research Question

The main question guiding this project is:

What behavioral patterns are most associated with a customer’s likelihood to respond to marketing campaigns?

To break this down further, I explored several subquestions:

Are higher-spending customers more likely to respond?
Does frequent browsing actually lead to engagement, or just interest?
Are deal-oriented customers more responsive to campaigns?
Do demographic factors like age or household structure matter?
Which types of spending are most associated with response?

## Methodology

This project is based on exploratory data analysis (EDA) using Python. I began by cleaning and preparing the dataset, then created new variables to better capture customer behavior. After that, I used visualizations and grouped summaries to identify patterns between customers who responded to the campaign and those who did not.

## Data Preparation

Before conducting any analysis, I cleaned the dataset by:
Removing rows with missing income values
Converting date variables into usable datetime format
Removing columns with no variation (constant values)
Checking for duplicates

Income was especially important to retain because it plays a role in many behavioral comparisons, so rows missing income were removed to maintain consistency.

## Feature Engineering (Creating New Variables)

To better capture behavior, I created several new variables:

Age: Calculated from year of birth

Total Spending: Combined spending across all product categories

Total Purchases: Combined purchases across web, store, and catalog

Children at Home: Combined number of kids and teens

Past Campaign Engagement: Total number of previously accepted campaigns

Browsing vs Buying Ratio: Website visits divided by purchases

Deal-Oriented Indicator: Whether a customer frequently purchases using deals

These variables helped move the analysis beyond raw data and into more meaningful behavioral patterns.

## Key Findings

1. Spending and Engagement:
One of the clearest patterns in the data is that customers who spend more are significantly more likely to respond to marketing campaigns. Higher total spending is associated with higher response rates, suggesting that more engaged or valuable customers are also more receptive to marketing. This supports the idea that active customers are already connected to the business, making them more likely to engage when targeted.

2. Purchasing Behavior vs Browsing Behavior:
A particularly interesting finding was the difference between browsing and purchasing behavior. Customers who frequently visit the website but do not make purchases tend to be less likely to respond to campaigns. In contrast, customers who convert visits into purchases are much more likely to engage. From a behavioral perspective, this suggests that action-based behavior (buying) is a stronger indicator of engagement than passive behavior (browsing).

3. Deal-Oriented Customers:
One surprising result was that deal-oriented customers were actually less likely to respond to campaigns. At first, it might seem like customers who look for deals would be more responsive to marketing. However, the data suggests that these customers may be more selective and only respond to very specific types of offers. This could mean that deal-oriented customers are not broadly engaged with the brand, but instead respond only when incentives meet their expectations.

4. Income and Spending Patterns:
There is a clear positive relationship between income and spending. Higher-income customers tend to spend more, although there is still a wide variation in behavior. This suggests that while income influences purchasing power, it does not fully determine engagement or responsiveness.

5. Demographics vs Behavior:
Demographic variables such as age showed very little difference between responders and non-responders. However, household structure had a more noticeable effect. Customers with fewer children at home were more likely to respond to campaigns. This may reflect differences in time, flexibility, or priorities, suggesting that lifestyle factors play a role in engagement.

## Interpretation

Overall, the results show that behavioral factors are much stronger predictors of campaign response than demographic characteristics. Customers who are already active, those who spend more and make more purchases, are the most likely to respond. On the other hand, customers who are less engaged or only casually browsing are much less likely to respond. This aligns with a behavioral perspective: people who are already interacting with a brand are more likely to continue that interaction.

## Limitations

There are several limitations to this analysis:
The dataset does not specify the type of marketing campaign
The analysis is observational and does not establish causation
Some potentially important psychological factors (motivation/preferences) are not included
There are some outliers and data limitations

Because of this, the findings should be interpreted as general patterns rather than definitive conclusions.

## Streamlit Application

To extend this project, I created an interactive Streamlit application that allows users to explore the dataset in a more dynamic way.

The app includes:
Filtering customers by income range
Viewing a preview of filtered data
Visualizing the relationship between income spending 

This allows users to move beyond static graphs and interact with the data directly. By adjusting inputs and exploring different segments, users can better understand how behavior changes across different groups. For example, the scatter plot of income versus wine spending shows a general positive relationship, but also highlights variability in customer behavior. This reinforces the idea that while income plays a role, it is not the only factor influencing spending.

## Deeper Behavioral Insights

One of the most interesting aspects of this project is how it highlights the difference between surface-level engagement and meaningful behavioral engagement. At first glance, metrics such as website visits or general activity might seem like strong indicators of customer interest. However, the analysis suggests that not all engagement is equal. Customers who frequently browse the website without making purchases appear to demonstrate curiosity or passive interest, but this does not translate into meaningful interaction with the brand. 
In contrast, customers who consistently make purchases show a much higher likelihood of responding to marketing campaigns. This suggests that behavioral commitment, rather than attention alone, is a more accurate measure of customer engagement. From a psychological perspective, this can be connected to the idea that actions reinforce preferences. When customers actively purchase products, they are not only spending money but also reinforcing their relationship with the brand, making them more receptive to future interactions.

Another important insight comes from the behavior of deal-oriented customers. Initially, it might be expected that customers who frequently use discounts would be more responsive to campaigns, since marketing often involves promotional offers. However, the findings suggest the opposite. Deal-oriented customers were less likely to respond overall, which may indicate that they are more selective and only engage when a campaign closely matches their expectations. This behavior reflects a more calculated decision-making process, where customers prioritize maximizing value rather than engaging broadly with the brand.

Additionally, the role of household structure provides a more subtle but meaningful perspective on customer behavior. Customers with fewer children at home were more likely to respond to campaigns, which may reflect differences in available time, financial flexibility, or attention. This suggests that engagement is not only influenced by individual preferences, but also by external lifestyle factors that shape how customers interact with businesses.
Overall, these patterns reinforce the idea that customer behavior is complex and cannot be fully understood through a single variable. Instead, it requires looking at how different behaviors interact. Spending, purchasing frequency, browsing habits, and lifestyle factors all contribute to shaping how customers respond to marketing efforts. By taking a more behavioral approach, this analysis provides a deeper understanding of engagement that goes beyond traditional metrics.

## Practical Implications

The findings from this analysis have several practical implications for how businesses approach marketing strategies. One key takeaway is that companies should prioritize targeting customers who are already actively engaged with their products. Rather than focusing on broad outreach to all potential customers, businesses may benefit more from identifying high-value individuals who frequently make purchases and tailoring campaigns specifically toward them.
Additionally, the results suggest that simply increasing website traffic may not be an effective strategy if it does not lead to purchases. Customers who browse frequently without converting do not appear to be strong candidates for campaign response. This means that businesses should focus not only on attracting attention, but also on improving conversion rates and encouraging meaningful interaction with their platforms.
The behavior of deal-oriented customers also has important implications. Since these customers are less likely to respond to general campaigns, businesses may need to design more targeted or personalized promotions for this group. Instead of relying on broad discounts, companies could experiment with more strategic incentives that align with specific customer preferences.

Finally, the findings highlight the importance of understanding customer behavior beyond basic demographics. While factors like age had little impact on response rates, behavioral patterns such as spending and purchasing activity were much more informative. This suggests that businesses should invest in data-driven approaches that focus on how customers interact with their brand over time.

## Conclusion

This project highlights the importance of understanding customer behavior when analyzing marketing effectiveness.
The results suggest that:
Active customers are more likely to respond
Purchasing behavior is more important than browsing
High-value customers are key targets for marketing
Behavioral patterns matter more than basic demographics

From a practical perspective, this means that businesses should focus on customers who are already engaged rather than relying solely on broad outreach strategies. From a personal perspective, this project reinforced my interest in behavioral analysis and how data can be used to better understand decision-making. Rather than just identifying trends, this approach allows for deeper insight into why customers behave the way they do.
