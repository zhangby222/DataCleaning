# handling non-standard missing values:
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("property data.csv", na_values = missing_values

# Impute the missing values with mean imputation
# cc_app only have four numeric columns and cc_app.mean() returns a 2*4 pd series in which the columnnames are the numeric columns names.
# this will fill all NaN entries with mean of that columns. (only works for four numeric columns)
cc_apps.fillna(cc_apps.mean(), inplace=True)

# Impute with the most frequent value
cc_apps = cc_apps.fillna(cc_apps[col].value_counts()[-1])

# Count the number of NaNs in each column 
np.sum(cc_apps.isnull())
