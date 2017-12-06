from bs4 import BeautifulSoup
from selenium import webdriver
stock_file = r"C:\Users\Tut10\Desktop\PSTool-Python\Final\test.txt"

def Costco_Shipping(url):
    """This opens up chrome. Scans through the webpage for the out of stock class
    prints out if in stock or out and writes it to file. Pretty simple
    """
    
    driver = webdriver.Chrome(r"C:\Users\Tut10\Desktop\PSTool-Python\chromedriver.exe")
    
    driver.get(url)
    
    file_to_write = open(stock_file, "a")
    
    try:
        x = driver.find_element_by_class_name("out-of-stock")
        if x:
            driver.quit()
            file_to_write.write("[-] Out of stock " + url + '\n')
            file_to_write.close()            
            return "\t\t[-] Out of Stock"
    except:
        driver.quit()
        file_to_write.close() 
        return "\t\t[+] In Stock"
    

def Home_Depot_Shipping(url):
    
    driver = webdriver.Chrome(r"C:\Users\Tut10\Desktop\PSTool-Python\chromedriver.exe")
    driver.get(url)
    
    # open a file to write to
    file_to_write = open(stock_file, "a")
    
    # send that file to me via email or text
    
    free_delivery = driver.find_elements_by_xpath(r'//*[@id="buybelt"]/div[2]/div[2]/div/div[2]')
    
    for x in free_delivery:
        
    
    # Now it checks
    #Free Delivery
    #Standard Delivery
        #print(x.text)
    
    
        try:
            if "Free Delivery" in x.text:
                driver.quit()
                file_to_write.close()
                return "\t\t[+] Free Delivery"
            elif "Get it as soon as tomorrow" in x.text:
                driver.quit()
                #file_to_write.write("Cell: " + str(cell) + "[*] Express Delivery " + url + '\n')
                file_to_write.write("[*] Express Delivery " + url + "\n")
                file_to_write.close()
                return "\t\t[*] Express Delivery"
            elif "Receive an email" in x.text:
                driver.quit()
                file_to_write.write("[-] Out of Stock %s\n" % url)
                file_to_write.close()
                return "\t\t[-] Out of stock!"
            elif "Standard Delivery" in x.text:
                driver.quit()
                file_to_write.close()
                return "\t\t[+] Standard Delivery"
            #else:    
                #driver.quit()
                #file_to_write.write("[-] Out of stock %s\n" % url)
                #file_to_write.close()
                #return "\t\t[-] Out of stock!"
        except Exception as e:
            driver.quit()
            print(e)    

def Kohls_Shipping(url):
    pass

def BedBathBeyond_Shipping(url):
    pass