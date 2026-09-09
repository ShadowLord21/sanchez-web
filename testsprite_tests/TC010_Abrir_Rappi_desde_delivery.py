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
        
        # -> Scroll to the 'Delivery' section on the page so the delivery channel cards (including 'Rappi') become visible.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Rappi' delivery link in the Delivery and Pedidos section to open the external delivery platform in a new tab.
        # Rappi link
        elem = page.get_by_role('link', name='Rappi', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The 'Rappi' delivery card opened a new browser tab that navigated to Rappi's site.
        # Assert-outcome: passed
        # Assert: The new tab's URL contains 'rappi.com.ar'.
        await expect(page).to_have_url(re.compile("rappi\\.com\\.ar"), timeout=15000), "The new tab's URL contains 'rappi.com.ar'."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    