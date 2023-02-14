#%%
import contextlib
import socket

def main_1() -> None:
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM
                           )
    server.bind(("localhost", 2401))
    server.listen(1)
    with contextlib.closing(server):
        while True:
            client, addr = server.accept()
            dice_response(client)
            client.close()
            
            
def dice_response(client: socket.socket) -> None:
    request = client.recv(1024)
    try:
        response = dice.dice_roller(request)
    except (ValueError, KeyError) as ex:
        response = repr(ex).encode('utf-8')
    client.send(response)
    
    
import random

def dice_roller(request: bytes) -> bytes:
    request_text = request.decode('utf-8')
    numbers = [random.randint(1, 6) for _ in range(6)]
    response = f"{request_text} = {numbers}"
    return response.encode("utf-8")







# Methodology
# The dataset analyzed is core-level raw measurements of tree-ring width from
# species such as Norway spruce, Scots pine, and Pedunculate oak with each species
# sampled from dorminant and suppressed category. The pointer year for the analysis is
# define to be 2003. Lloret et al. 2011 concept ot resilience forms the basis for analyzing
# growth resilience. Growth resilience was defined to be the resilience component of the
# resilience indices by Lloret et al. 2011.
# To prepare the data for estimation of resilience, tree means of tree ring widths were
# computed based on grouping tree cores per each tree species. Further the data was detrended,
# to normalize the influence of other exgenuous factors on tree ring growth.

# In determining the method to employ for the analysis, a number of exploratory technique
# including both visualization and statistical test to determine whether underlying assumptions have
# have been met were undertaken to chose the method of analysis from parametric and non-parametric
# methods.
# This included histograms to visualize the distribution of the data and boxplot to
# depict variance among tree species. Shapiro wirk test was undertaken to determine if
# distribution of data point was from a normal distribution. Homogeneity among tree species was
# tested using Bartlet test which is well cut out for a normally distributed data. The result
# was verified using other methods such as the Levene test. For the various statistical test
# 95% confidence interval was define as the threshold to decide whether to reject or fail to
# reject the null hypothesis.

# With regards to quantifying and determining whether  differences in growth resilience
# between Norway spruce dorminant, Scots pine dorminant, and Pedunculate oak dorminant
# is statistically significant, Analysis of Varaince (ANOVA) method was used based on
# hypothesis framework define as follows;
# H0: There is no statistically significant difference in the mean resilience value among
# various dorminant tree species
# H1: There is statistically significant difference in the mean resilience value
# of various dorminant tree species

# For analysis of suppressed and dorminant various tree species, the hypothesis was
# defined per tree species comparing the mean tree resilience value for that tree
# species. This produced a two sample t-test and for Norway spruce as an example,
# the hypothesis is framed as follows;

# H0: There is no statistically significant difference in the mean resilience value between
# various Norway spruce dorminant and norway spruce suppressed

# H1: There is statistically significant difference in the mean resilience value between
# various Norway spruce dorminant and norway spruce suppressed

# The hypothesis for Pedunculate oak dominant and Pedunculate oak suppressed is stated as
# follows
# H0: There is no statistically significant difference in the mean resilience value between
# various Pedunculate oak dominant and Pedunculate oak suppressed

# H1: There is statistically significant difference in the mean resilience value between
# various Pedunculate oak dominant and Pedunculate oak suppressed


# The hypothesis for Scots pine dorminant and Scot pine suppressed is defined as follows
# H0: There is no statistically significant difference in the mean resilience value between
# Scots pine dorminant and Scot pine suppressed

# H1: There is statistically significant difference in the mean resilience value between
# Scots pine dorminant and Scot pine suppressed



# RESULTS
# The results for the research questions defined is preceeded by exploratory visualizations
# and results of asummption testing as follows

# Figure 1: Illustrates visualization of detrended tree ring width for various tree species

# Figure 2: Illustrates histogram of resilience values of various tree species depicting
# normal distribution

# Figure 3: Illustrates boxplot of resilience values of the various tree species

# Figure 4: Illustrates shapiro wilk tests

# Figure 5: shows the result of anova test for dorminant tree species


# Interpretation

# The sample size of the tree species is generally small.
# The density plots and histograms of all dorminant tree species shows a normally
# distributed data point. This is supported by the Shapiro Wilk statistical test where the null
# hypothesis fail to be rejected at 95% confidence interval for all tree species.
# In figure X, the p-value is 0.4114 hence we fail to reject null hypothesis
# that the distribution of Norway spruce dorminant is not statistically significantly
# different from a normal distribution at a 95% confidence level. In the case of
# Pedunculate Oak, the p-value of 0.8461 suggest that the null hypothesis of distribution
# not being statistically significantly different from normal distribution fails to
# be rejected at 95% confidence interval. In a similar manner, p-value of 0.2142 for
# Scots Pine resilience data points distributions led to not rejecting the hypothesis
# that it is a normal distribution. On the basis of these exploratory results, the
# assumption of normal distribution has been proven for a parametric test to be used for
# to testing variance.

# The result for homogeneity test using bartlet test produced a p-value of 0.481
# indicating variance is equal among all dorminant tree species hence
# the null hypothesis of homogeneity fails to be rejected. With the assumption of normality
# and homogeneity satisfied, parametric method was employed to quantify and test
# whether there is statistically significant difference in resilience level among dorminant
# trees.


# In response to the objective of quantifying the difference between dorminant trees,
# the anova result shows a p-value of 0.0685 hence we fail to reject the null hypothesis
# at 95% confidence interval. This means that mean resilience value is equal
# among norway spruce, pedunculate oak and scots pine dorminant trees

# Focusing on whether there is a significant difference between resilience
# level (mean) between dorminant and suppressed Scot Pine species,
# p-value of 0.367  translates that
# there is no difference in the mean value of the resilience level between
# Scots Pine dorminant and suppress trees. In a similar manner,
# there is no difference in the mean value of the resilience level between
# pedunculate oak dorminant and suppress trees based on a p-value of 0.457 (95% confidence interval)
# This interpretation equally holds true for Norway spruce where
# p-value is 0.235 hence
# there is no difference in the mean value of resilience between
# norway spruce dorminant and suppress trees


# CONCLUSION
# It is concluded that irrespective of the type of tree species and group from which it is
# sampled (dorminant and suppressed), resilience level does not differ.







    