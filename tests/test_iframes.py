from playwright.sync_api import expect, Keyboard
from utilities.utilities import set_test_status
import re


def test_nested_iframe_can_be_loaded_correctly(page):
    """
    Test nested iframes can be rendered correctly with the lambdatest blog website.
    Search for blogs by author Jaydeep Karale. Verify that the blog How To Use Playwright For Web Scraping with Python exists
    Also verify that author profile contains correct link 
    """    
    try:
        page.goto('https://codepen.io/jaydeepkarale/pen/dygvXbm')    
        base_frame_locator = page.frame_locator("iframe[name=\"CodePen\"]").frame_locator("#frame1")    
        base_frame_locator.get_by_placeholder("Enter a url").fill("https://www.lambdatest.com/blog")
        base_frame_locator.get_by_role("button", name="Render iframe").click()    
        base_frame_locator.frame_locator('#iframe-window').get_by_placeholder("Search …").fill('Jaydeep')
        page.keyboard.press('Enter')    
        blog_link_locator = base_frame_locator.frame_locator('#iframe-window').get_by_role('link', name='How To Use Playwright For Web Scraping with Python').first
        blog_author_locator = base_frame_locator.frame_locator('#iframe-window').get_by_role('link', name='Jaydeep Karale').first
        expect(blog_link_locator).to_have_attribute('href',re.compile('/blog/playwright-for-web-scraping/'))
        expect(blog_author_locator).to_have_attribute('href','https://www.lambdatest.com/blog/author/jaydkarale/')
        set_test_status(page, 'Passed','Blog exists')
        page.close()
    except Exception as ex:
        set_test_status(page, 'Failed',str(ex))
     


def test_iframe_tester_blogs_visible(page):
    """Test if iframe renders the lambdatest blog URL correctly.
    CLick on Book A Demo and fill the form with company name, firstname, lastname, email and phonenumber    
    """
    
    try:
        page.goto('https://iframetester.com/')
        page.get_by_placeholder('Enter a url').fill('https://www.lambdatest.com/blog')
        page.keyboard.press('Enter')        
        page.frame_locator('#iframe-window').get_by_role('link', name='Book A Demo', exact=True).click()    
        page.frame_locator("internal:text=\"<p>Your browser does not support iframes.</p>\"i").get_by_text("Allow Cookie").click()
        page.frame_locator("internal:text=\"<p>Your browser does not support iframes.</p>\"i").get_by_placeholder("Company Name").fill('Test Company')
        page.frame_locator("internal:text=\"<p>Your browser does not support iframes.</p>\"i").get_by_role("textbox", name="First Name*").fill('Test First Name')
        page.frame_locator("internal:text=\"<p>Your browser does not support iframes.</p>\"i").get_by_role("textbox", name="Last Name*").fill('Test Last Name')
        page.frame_locator("internal:text=\"<p>Your browser does not support iframes.</p>\"i").get_by_role("textbox", name="Work Email*").fill('sample@sample.com')
        page.frame_locator("internal:text=\"<p>Your browser does not support iframes.</p>\"i").get_by_role("textbox", name="Phone Number*").fill('1234567890')                        
        set_test_status(page, 'Passed','Form input completed')
        page.close()
    except Exception as ex:        
        set_test_status(page, 'Failed',str(ex))
