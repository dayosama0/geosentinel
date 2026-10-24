"""Smoke checks for the local UX prototype (not tests of backend or ML)."""
from pathlib import Path
from playwright.sync_api import sync_playwright

repo = Path(__file__).resolve().parent.parent
html = (repo / 'prototype' / 'prototype.html').read_text(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path='/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None, args=['--no-sandbox'])
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.set_content(html, wait_until='load')
    for name in ['overview', 'citizen', 'missions', 'alerts', 'history', 'models']:
        page.locator(f'[data-view="{name}"]').click()
        assert page.locator('h1').count() == 1
    page.locator('[data-view="citizen"]').click()
    page.locator('[data-action="status"]').click()
    assert 'Track a submitted report' in page.locator('h1').inner_text()
    page.locator('[data-view="citizen"]').click()
    sample = (repo / 'prototype' / 'screenshots' / '01_inspector_overview.png').read_bytes()
    page.locator('#photo').set_input_files({'name': 'example.png', 'mimeType': 'image/png', 'buffer': sample})
    page.locator('#location-picker').click(position={'x': 60, 'y': 55})
    assert page.locator('#photo').evaluate('(el) => el.files.length') == 1
    assert page.locator('#coordinates').input_value() == 'Point selected'
    page.locator('#citizen-form button[type=submit]').click()
    assert 'Reference' in page.locator('#app-content').inner_text()
    page.locator('[data-view="missions"]').click()
    page.locator('#mission-outcome').select_option('Waste present')
    page.locator('[data-action="completeMission"]').click()
    assert 'Completed' in page.locator('#app-content').inner_text()
    page.locator('[data-view="alerts"]').click()
    page.locator('[data-action="testOld"]').click()
    assert 'Rule check passed' in page.locator('#toast').inner_text()
    assert not errors, errors
    browser.close()
print('PASS: navigation, public status, file/location preservation, report, mission outcome, old-image alert check; no JS errors')
