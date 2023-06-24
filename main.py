def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    number_of_males = int(input("What's is the number of males registered in the class?:  "))
    number_of_females = int(input("What's is the number of females registered in the class?:  "))
    
    total_number_of_students = number_of_males+number_of_females
    m_perc = (number_of_males /  total_number_of_students) * 100
    f_perc = (number_of_females /  total_number_of_students) *100
    
    print (total_number_of_students)
    print (number_of_females,number_of_males)

    print (f'The percentage of females: \t {f_perc: .2f}') 
    print (f'The percentage of males: \t {m_perc: .2f}') 




    """
    
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
