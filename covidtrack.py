import requests
import time
from bs4 import BeautifulSoup as bs


def get_info(country_name):
    url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"
    data = requests.get(url)
    soup = bs(data.text, 'html.parser')
    
    cases = soup.find_all("div", class_="maincounter-number")
    total = cases[0].text
    total = total[1: len(total) - 2]
    recovered = cases[2].text
    recovered = recovered[1: len(recovered) - 1]
    deaths = cases[1].text
    deaths = deaths[1: len(deaths) - 1]

    numbers = {'Total Cases': total, 'Recovered Cases': recovered,
               'Total Deaths': deaths}
    return numbers


def main():
    while True:
        try:
            country_name = input("\nEnter A country name (ex: us, benin, india... ): ")
            country_data = get_info(country_name)
            print("\nCases in " + country_name + " :")
            for i, j in country_data.items():
                print(i + " : " + j)
        except IndexError:
            print('\nSorry, no data for this country')
            print('\nTry re-formatting the country name (US/UK/USA/France...)')

        time.sleep(3)

        choice = input("\nWanna see more? Enter 'yes' or 'no': ").lower()
        if choice == 'yes':
            pass
        elif choice == 'no':
            print('\nGoodbye...')
            time.sleep(2)
            break
        else:
            print("\nSorry, try again")
            continue


if __name__ == "__main__":
    main()
