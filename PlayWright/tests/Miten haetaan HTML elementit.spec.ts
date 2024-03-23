import {test} from '@playwright/test'

test.beforeEach(async({page}) => {
	await page.goto('http://localhost:4200/')
	await page.getByText('Forms').click()
	await page.getByText('Form Layouts').click()
})

test('Eka testi', async({page}) => {

	//locator method
    // remember to add await at the beginning when needed 

	//by Tag name 
	//await page.locator('input').click()

    //by Tag name  (first clicks the first element if there is many of same name)
	await page.locator('input').first().click()

	//by ID
	page.locator('#inputEmail')

	//by Class value
	page.locator('.shape-rectangle')

	//by attribute
	page.locator('[palceholder="Email"]')

	//by Class value (full)
	page.locator('[class="calssfullname-asns908098321433+23432"]')

	//Combine different selectors
	page.locator('input[placeholder="Email"][otherSelectorName]')

	//by XPath (NOT RECOMENDDED)
	page.locator('//*[@id="inputEmail"]')

	//by partial text match
	page.locator(':text("add the text here")')

	//by exact text match
	page.locator(':text-is"add the exact text here"')
})

test('Toinen testi', async({page}) => {
	
	//getByRole method
	await page.getByRole('textbox', {name: "Email"}).first().click()
	await page.getByRole('button', {name: "Sign in"}).first().click()
	
	//getByLable method
	await page.getByLabel('Email').first().click()

	//getByPlaceholder
	await page.getByPlaceholder('First name').first().click()
	
	//getByText
	await page.getByText('Using the Grid').first().click()

	//getByTestId
	page.getByTestId('omaSignInid').click()

	//getByTitle
	await page.getByTitle('IoT Dashboard').click()

})
