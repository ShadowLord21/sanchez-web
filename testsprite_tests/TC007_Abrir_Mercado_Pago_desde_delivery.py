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
        
        # -> Scroll the page to the Delivery section and reveal the payment options so the 'Mercado Pago' card becomes visible.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Mercado Pago' link in the Delivery and Pedidos section and verify a new tab opens to the external Mercado Pago site.
        # Mercado Pago link
        elem = page.get_by_role('link', name='Mercado Pago', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Clicking the 'Mercado Pago' link opened a new tab to the external Mercado Pago domain (mpago.li).
        # Assert-outcome: passed
        # Assert: Browser navigated to a URL containing 'mpago.li'.
        await expect(page).to_have_url(re.compile("mpago\\.li"), timeout=15000), "Browser navigated to a URL containing 'mpago.li'."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    