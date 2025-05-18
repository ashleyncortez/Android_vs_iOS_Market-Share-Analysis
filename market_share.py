import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your CSV file
df = pd.read_csv('data/mobile_os_share_feb_apr_2025.csv', encoding='utf-8')
print(df)


# Preview column names to confirm structure
print("Columns:", df.columns)

# Standardize column names and keep only relevant ones
df = df[['Continent', 'Android', 'iOS']].copy()
df.rename(columns={'Continent': 'Country'}, inplace=True)

# Clean up country names
df['Country'] = df['Country'].str.strip()

# Map territories to parent countries
territory_map = {
    'American Samoa': 'United States of America',
    'Anguilla': 'United Kingdom',
    'Aruba': 'Netherlands',
    'Bermuda': 'United Kingdom',
    'British Virgin Islands': 'United Kingdom',
    'Cayman Islands': 'United Kingdom',
    'Christmas Island': 'Australia',
    'Curaçao': 'Netherlands',
    'Faroe Islands': 'Denmark',
    'French Guiana': 'France',
    'French Polynesia': 'France',
    'Gibraltar': 'United Kingdom',
    'Greenland': 'Denmark',
    'Guadeloupe': 'France',
    'Guam': 'United States of America',
    'Isle of Man': 'United Kingdom',
    'Jersey': 'United Kingdom',
    'Macau': 'China',
    'Martinique': 'France',
    'Mayotte': 'France',
    'Montserrat': 'United Kingdom',
    'New Caledonia': 'France',
    'Niue': 'New Zealand',
    'Northern Mariana Islands': 'United States of America',
    'Palestinian Territory': 'Israel',
    'Puerto Rico': 'United States of America',
    'Réunion': 'France',
    'Saint Barthélemy': 'France',
    'Saint Helena': 'United Kingdom',
    'Saint Martin': 'France',
    'Saint Pierre and Miquelon': 'France',
    'Sint Maarten': 'Netherlands',
    'Svalbard & Jan Mayen Islands': 'Norway',
    'Tokelau': 'New Zealand',
    'Turks and Caicos Islands': 'United Kingdom',
    'US Virgin Islands': 'United States of America',
    'Wallis and Futuna': 'France',
    'Guernsey': 'United Kingdom',
    'Saint Barthelemy': 'France',
}

# Apply territory remapping
df['Country'] = df['Country'].replace(territory_map)

# Group by country and calculate average OS share
df_grouped = df.groupby('Country', as_index=False)[['Android', 'iOS']].mean()

# Display top 10 Android and iOS countries
top_android = df_grouped.sort_values(by='Android', ascending=False).head(10)
top_ios = df_grouped.sort_values(by='iOS', ascending=False).head(10)

print("\nTop Android Countries:")
print(top_android)

print("\nTop iOS Countries:")
print(top_ios)

# Set seaborn style
sns.set(style='whitegrid')

# Android-dominant countries
plt.figure(figsize=(12, 6))
sns.barplot(x='Android', y='Country', data=top_android, palette='viridis')
plt.title('Top 10 Countries by Android Market Share')
plt.xlabel('Android Share (%)')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

# iOS-dominant countries
plt.figure(figsize=(12, 6))
sns.barplot(x='iOS', y='Country', data=top_ios, palette='mako')
plt.title('Top 10 Countries by iOS Market Share')
plt.xlabel('iOS Share (%)')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

# Side-by-side comparison
top_combined = df_grouped.sort_values(by='Android', ascending=False).head(10)
melted = top_combined.melt(id_vars='Country', value_vars=['Android', 'iOS'])

plt.figure(figsize=(12, 6))
sns.barplot(x='value', y='Country', hue='variable', data=melted)
plt.title('Top 10 Countries by Android Share (with iOS Comparison)')
plt.xlabel('Share (%)')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

us_ios = df_grouped[df_grouped['Country'] == 'United States of America']
print(us_ios)

# --- Top Android + U.S. ---
top_android = df_grouped.sort_values(by='Android', ascending=False).head(10)
us_row = df_grouped[df_grouped['Country'] == 'United States of America']

# Append U.S. if not already there
top_android_plus_us = pd.concat([top_android, us_row]).drop_duplicates(subset='Country')
top_android_plus_us = top_android_plus_us.sort_values(by='Android', ascending=False)

# --- Top iOS + U.S. ---
top_ios = df_grouped.sort_values(by='iOS', ascending=False).head(10)
top_ios_plus_us = pd.concat([top_ios, us_row]).drop_duplicates(subset='Country')
top_ios_plus_us = top_ios_plus_us.sort_values(by='iOS', ascending=False)

# Android plot
plt.figure(figsize=(12, 6))
sns.barplot(x='Android', y='Country', data=top_android_plus_us, palette='viridis')
plt.title('Top Android Market Share Countries (Including United States)')
plt.xlabel('Android Share (%)')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

# iOS plot
plt.figure(figsize=(12, 6))
sns.barplot(x='iOS', y='Country', data=top_ios_plus_us, palette='mako')
plt.title('Top iOS Market Share Countries (Including United States)')
plt.xlabel('iOS Share (%)')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

# Filter for United States data
us_data = df_grouped[df_grouped['Country'] == 'United States of America']

# Melt to long format for easier plotting
us_melted = us_data.melt(id_vars='Country', value_vars=['Android', 'iOS'], var_name='OS', value_name='Share')

plt.figure(figsize=(8, 4))
sns.barplot(data=us_melted, x='Share', y='OS', palette='pastel')
plt.title('Mobile OS Market Share in the United States')
plt.xlabel('Share (%)')
plt.ylabel('')
plt.xlim(0, 100)
plt.tight_layout()
plt.show()

# Mobile OS Market Share: US vs India
countries_to_compare_v1 = ['United States of America', 'India']  

# Filter and reshape
comparison_df = df_grouped[df_grouped['Country'].isin(countries_to_compare_v1)]
melted = comparison_df.melt(id_vars='Country', value_vars=['Android', 'iOS'], var_name='OS', value_name='Share')


plt.figure(figsize=(10, 6))
sns.barplot(data=melted, x='Country', y='Share', hue='OS', palette='Set2')
plt.title('Mobile OS Market Share: U.S. vs India')
plt.ylabel('Share (%)')
plt.xlabel('')
plt.ylim(0, 100)
plt.legend(title='OS')
plt.tight_layout()
plt.show()


# Mobile OS Market Share: US vs Canada
countries_to_compare_v2 = ['United States of America', 'Canada']  

# Filter and reshape
comparison_df = df_grouped[df_grouped['Country'].isin(countries_to_compare_v2)]
melted = comparison_df.melt(id_vars='Country', value_vars=['Android', 'iOS'], var_name='OS', value_name='Share')


plt.figure(figsize=(10, 6))
sns.barplot(data=melted, x='Country', y='Share', hue='OS', palette='Set2')
plt.title('Mobile OS Market Share: U.S. vs Canada')
plt.ylabel('Share (%)')
plt.xlabel('')
plt.ylim(0, 100)
plt.legend(title='OS')
plt.tight_layout()
plt.show()


# Mobile OS Market Share: US vs Australia
countries_to_compare_v3= ['United States of America', 'Australia']  

# Filter and reshape
comparison_df = df_grouped[df_grouped['Country'].isin(countries_to_compare_v3)]
melted = comparison_df.melt(id_vars='Country', value_vars=['Android', 'iOS'], var_name='OS', value_name='Share')


plt.figure(figsize=(10, 6))
sns.barplot(data=melted, x='Country', y='Share', hue='OS', palette='Set2')
plt.title('Mobile OS Market Share: U.S. vs Australia')
plt.ylabel('Share (%)')
plt.xlabel('')
plt.ylim(0, 100)
plt.legend(title='OS')
plt.tight_layout()
plt.show()

# Mobile OS Market Share: US vs Germany
countries_to_compare_v4= ['United States of America', 'Germany']  

# Filter and reshape
comparison_df = df_grouped[df_grouped['Country'].isin(countries_to_compare_v4)]
melted = comparison_df.melt(id_vars='Country', value_vars=['Android', 'iOS'], var_name='OS', value_name='Share')


plt.figure(figsize=(10, 6))
sns.barplot(data=melted, x='Country', y='Share', hue='OS', palette='Set2')
plt.title('Mobile OS Market Share: U.S. vs Germany')
plt.ylabel('Share (%)')
plt.xlabel('')
plt.ylim(0, 100)
plt.legend(title='OS')
plt.tight_layout()
plt.show()


import plotly.express as px

# Clean fill
df_grouped['iOS'] = df_grouped['iOS'].fillna(0)

# Plot iOS map
fig = px.choropleth(
    df_grouped,
    locations='Country',
    locationmode='country names',
    color='iOS',
    color_continuous_scale='Blues',
    title='Global iOS Market Share by Country (%)',
    labels={'iOS': 'iOS Share (%)'}
)

fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
fig.show()


#Plot Android Map
df_grouped['Android'] = df_grouped['Android'].fillna(0)

# Plot
fig = px.choropleth(
    df_grouped,
    locations='Country',
    locationmode='country names',
    color='Android',
    color_continuous_scale='Greens',
    title='Global Android Market Share by Country (%)',
    labels={'Android': 'Android Share (%)'}
)

fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
fig.show()
