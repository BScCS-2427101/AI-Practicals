#T101 RAJDEEP M PARAB
# Employee Promotion Probability Example
employee_examples = dict(
    e1=dict(Perf='H', Exp='H', Train='Y', Attend='Y', Promo='Y'),
    e2=dict(Perf='L', Exp='L', Train='N', Attend='N', Promo='N'),
    e3=dict(Perf='H', Exp='H', Train='Y', Attend='Y', Promo='Y'),
    e4=dict(Perf='H', Exp='L', Train='Y', Attend='Y', Promo='Y'),
    e5=dict(Perf='L', Exp='H', Train='N', Attend='Y', Promo='N'),
    e6=dict(Perf='H', Exp='H', Train='N', Attend='Y', Promo='Y'),
    e7=dict(Perf='L', Exp='L', Train='Y', Attend='N', Promo='N'),
    e8=dict(Perf='H', Exp='L', Train='Y', Attend='Y', Promo='Y'),
    e9=dict(Perf='L', Exp='H', Train='N', Attend='N', Promo='N'),
    e10=dict(Perf='H', Exp='H', Train='Y', Attend='Y', Promo='Y'),
    e11=dict(Perf='L', Exp='L', Train='N', Attend='Y', Promo='N'),
    e12=dict(Perf='H', Exp='L', Train='N', Attend='Y', Promo='Y')
)
total_emp = 12

# Count occurrences of an attribute value
def tot(attribute, value):
    count = 0
    for key, val in employee_examples.items():
        if val[attribute] == value:
            count += 1
    return count

# Calculate conditional probability
def getProbab(attribute, attribval, value):
    count = 0
    for key, val in employee_examples.items():
        if val[attribute] == attribval and val['Promo'] == value:
            count += 1
    probab = count / tot('Promo', value)
    return probab

def main():
    # Prior probabilities
    PPromoYes = tot('Promo', 'Y') / total_emp
    PPromoNo = tot('Promo', 'N') / total_emp

    # Performance probabilities
    PPerfHigh = tot('Perf', 'H') / total_emp
    PPerfLow = tot('Perf', 'L') / total_emp

    # Experience probabilities
    PExpHigh = tot('Exp', 'H') / total_emp
    PExpLow = tot('Exp', 'L') / total_emp

    # Training probabilities
    PTrainYes = tot('Train', 'Y') / total_emp
    PTrainNo = tot('Train', 'N') / total_emp

    # Attendance probabilities
    PAttendYes = tot('Attend', 'Y') / total_emp
    PAttendNo = tot('Attend', 'N') / total_emp

    # Performance
    print("Probability of Promotion for HIGH Performance:")
    print(
        "Promotion Yes:",
        round(
            (getProbab('Perf', 'H', 'Y')
             * PPromoYes / PPerfHigh) * 100,
            2
        ),
        "%"
    )
    print(
        "Promotion No :",
        round(
            (getProbab('Perf', 'H', 'N')
             * PPromoNo / PPerfHigh) * 100,
            2
        ),
        "%"
    )
    print("\nProbability of Promotion for LOW Performance:")
    print(
        "Promotion Yes:",
        round(
            (getProbab('Perf', 'L', 'Y')
             * PPromoYes / PPerfLow) * 100,
            2
        ),
        "%"
    )
    print(
        "Promotion No :",
        round(
            (getProbab('Perf', 'L', 'N')
             * PPromoNo / PPerfLow) * 100,
            2
        ),
        "%"
    )

    # Experience
    print("\nProbability of Promotion for HIGH Experience:")
    print(
        "Promotion Yes:",
        round(
            (getProbab('Exp', 'H', 'Y')
             * PPromoYes / PExpHigh) * 100,
            2
        ),
        "%"
    )
    print(
        "Promotion No :",
        round(
            (getProbab('Exp', 'H', 'N')
             * PPromoNo / PExpHigh) * 100,
            2
        ),
        "%"
    )
    print("\nProbability of Promotion for LOW Experience:")
    print(
        "Promotion Yes:",
        round(
            (getProbab('Exp', 'L', 'Y')
             * PPromoYes / PExpLow) * 100,
            2
        ),
        "%"
    )
    print(
        "Promotion No :",
        round(
            (getProbab('Exp', 'L', 'N')
             * PPromoNo / PExpLow) * 100,
            2
        ),
        "%"
    )

    # Training
    print("\nProbability of Promotion if Training is Completed:")
    print(
        "Promotion Yes:",
        round(
            (getProbab('Train', 'Y', 'Y')
             * PPromoYes / PTrainYes) * 100,
            2
        ),
        "%"
    )
    print(
        "Promotion No :",
        round(
            (getProbab('Train', 'Y', 'N')
             * PPromoNo / PTrainYes) * 100,
            2
        ),
        "%"
    )
    print("\nProbability of Promotion if Training is NOT Completed:")
    print(
        "Promotion Yes:",
        round(
            (getProbab('Train', 'N', 'Y')
             * PPromoYes / PTrainNo) * 100,
            2
        ),
        "%"
    )
    print(
        "Promotion No :",
        round(
            (getProbab('Train', 'N', 'N')
             * PPromoNo / PTrainNo) * 100,
            2
        ),
        "%"
    )
    # Attendance
    print("\nProbability of Promotion if Attendance is Good:")
    print(
        "Promotion Yes:",
        round(
            (getProbab('Attend', 'Y', 'Y')
             * PPromoYes / PAttendYes) * 100,
            2
        ),
        "%"
    )
    print(
        "Promotion No :",
        round(
            (getProbab('Attend', 'Y', 'N')
             * PPromoNo / PAttendYes) * 100,
            2
        ),
        "%"
    )
    print("\nProbability of Promotion if Attendance is Poor:")
    print(
        "Promotion Yes:",
        round(
            (getProbab('Attend', 'N', 'Y')
             * PPromoYes / PAttendNo) * 100,
            2
        ),
        "%"
    )
    print(
        "Promotion No :",
        round(
            (getProbab('Attend', 'N', 'N')
             * PPromoNo / PAttendNo) * 100,
            2
        ),
        "%"
    )
main()
