# importing plotting tools
import matplotlib.pyplot as plt
# importing school_scores database and python api
import school_scores

years = []
AL_scores = []
MA_scores = []

scores = school_scores.get_all()

print(scores[0]["Gender"]["Female"]["Math"])

for row in (scores):
    print(row["State"]["Name"],row["Year"])

#for thisCurrentScore in scores:
#    print(thisCurrentScore)

#for currentScore in scores:
#    if currentScore["State"]["Code"] == 'AL':
    #    AL_scores.append(currentScore["Total"]["Math"])
    #    years.append([currentScore["Year"]])
#    elif currentScore["State"]["Code"] == 'MA':
#        MA_scores.append(currentScore["Total"]["Math"])

plt.plot(years,AL_scores)
plt.plot(years,MA_scores)
plt.legend(['AL','MA'], loc='upper left')

plt.xlabel('Years')
plt.ylabel('Scores')
plt.title('Average Math SAT scores in AL and MA')

plt.show()
