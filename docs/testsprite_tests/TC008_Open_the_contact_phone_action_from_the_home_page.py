import asyncio
import re
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None

    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()

        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",
                "--disable-dev-shm-usage",
                "--ipc=host",
                "--single-process"
            ],
        )

        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        # Wider default timeout to match the agent's DOM-stability budget;
        # auto-waiting Playwright APIs (expect, locator.wait_for) inherit this.
        context.set_default_timeout(15000)

        # Open a new page in the browser context
        page = await context.new_page()

        # Interact with the page elements to simulate user flow
        # -> navigate
        await page.goto("http://localhost:8000/estilo-floria/")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Scroll to the Contact section and locate the phone link or visible phone number in the Contacto / Contact section.
        await page.mouse.wheel(0, 300)
        
        # -> Click the '11 5927-3756' phone link in the Contacto section to verify the call action is available.
        # 11 5927-3756 link
        elem = page.get_by_text('Av. Rivadavia 3399', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='11 5927-3756', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The contact phone link '11 5927-3756' is present in the footer and provides a tel: call link.
        await page.locator("xpath=/html/body/footer/div/div/div[3]/ul/li[1]/a").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: The phone link '11 5927-3756' is visible in the footer.
        await expect(page.locator("xpath=/html/body/footer/div/div/div[3]/ul/li[1]/a").nth(0)).to_be_visible(timeout=15000), "The phone link '11 5927-3756' is visible in the footer."
        # Assert-outcome: passed
        # Assert: The phone link's href is a tel: link to initiate a call.
        await expect(page.locator("xpath=/html/body/footer/div/div/div[3]/ul/li[1]/a").nth(0)).to_have_attribute("href", "tel:+5491159273756", timeout=15000), "The phone link's href is a tel: link to initiate a call."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    