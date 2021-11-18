def miles_to_laps(miles_laps):
    return(miles_laps/0.25)

if __name__ == '__main__': 
    miles_laps=float(input())
    print('{:.2f}'.format(miles_to_laps(miles_laps)))