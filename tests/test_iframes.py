from playwright.sync_api import expect, Keyboard
from utilities.utilities import set_test_status
import re


def test_nested_iframe_can_be_loaded_correctly(page):
    """
    Test nested iframes
    """    
    try:
        page.goto('https://codepen.io/jaydeepkarale/pen/dygvXbm')    
        base_frame_locator = page.frame_locator("iframe[name=\"CodePen\"]").frame_locator("#frame1")    
        base_frame_locator.get_by_placeholder("Enter a url").fill("https://www.lambdatest.com/blog")
        base_frame_locator.get_by_role("button", name="Render iframe").click()    
        base_frame_locator.frame_locator('#iframe-window').get_by_placeholder("Search …").fill('Jaydeep')
        page.keyboard.press('Enter')    
        blog_link_locator = base_frame_locator.frame_locator('#iframe-window').get_by_role('link', name='How To Use Playwright For Web Scraping with Python').first
        expect(blog_link_locator).to_have_attribute('href',re.compile('/blog/playwright-for-web-scraping/'))
        set_test_status(page, 'Passed','Blog exists')
        page.close()
    except Exception as ex:
        set_test_status(page, 'Failed',str(ex))
     


def test_iframe_tester_blogs_visible(page):
    """Test if iframe renders the lambdatest blog URL correctly.
    Search for blogs by Jaydeep and check if Playwright locators blog exists
    and profile url of author is correct
    """
    try:
        page.goto('https://iframetester.com/')
        page.get_by_placeholder('Enter a url').fill('https://www.lambdatest.com/blog')
        page.keyboard.press('Enter')
        page.frame_locator('#iframe-window').get_by_placeholder('Search …').fill("Jaydeep")
        page.keyboard.press('Enter')
        blog_link_locator = page.frame_locator('#iframe-window').get_by_role('link', name='How To Find Elements Using Playwright Locators').first
        blog_author_locator = page.frame_locator('#iframe-window').get_by_role('link', name='Jaydeep Karale').first
        expect(blog_link_locator).to_have_attribute('href',re.compile('/playwright-locators/'))
        expect(blog_author_locator).to_have_attribute('href','https://www.lambdatest.com/blog/author/jaydkarale/')
        set_test_status(page, 'Passed','Author URL is correct')
        page.close()
    except Exception as ex:
        set_test_status(page, 'Failed',str(ex))

