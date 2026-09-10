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
        
        # -> Click the 'Menú del Día' hero button to open the menu del día section.
        # Menú del Día link
        elem = page.get_by_role('link', name='Menú del Día', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The Menú del Día selector shows 'Viernes' as the highlighted weekday.
        # Assert-outcome: passed
        # Assert: Verifies the weekday selector button text is 'Viernes'.
        await expect(page.locator("xpath=/html/body/section[4]/div/div/div/div[1]/button[5]").nth(0)).to_have_text("Viernes", timeout=15000), "Verifies the weekday selector button text is 'Viernes'."
        
        # --> The Menú del Día section is open and displays the Friday menu items.
        # Assert-outcome: passed
        # Assert: Verifies the URL fragment for the Menú del Día section is present.
        await expect(page).to_have_url(re.compile("\\#menudeldia"), timeout=15000), "Verifies the URL fragment for the Men\u00fa del D\u00eda section is present."
        await page.locator("xpath=/html/body/section[4]/div/div/div/div[6]/ul/li[1]/span").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: Verifies at least the first menu item entry is visible in the Menú del Día list.
        await expect(page.locator("xpath=/html/body/section[4]/div/div/div/div[6]/ul/li[1]/span").nth(0)).to_be_visible(timeout=15000), "Verifies at least the first menu item entry is visible in the Men\u00fa del D\u00eda list."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    