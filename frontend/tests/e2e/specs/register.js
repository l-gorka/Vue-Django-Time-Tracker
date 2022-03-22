// before runnning any of tests, execute 'python3 manage.py testserver users'
// to load user data

describe('Registaration test.', () => {

    it('the user can open registration modal by clicking at navbar icon', () => {
        cy.visit('/')
        cy.contains('Time tracker')
        cy.get('.nav-btn-register').click()
        cy.contains('Register new Account')
    })

    it('the user can not register with empty fields', () => {
        cy.get('.btn-register-submit').click()
        cy.contains('3-20 characters, starting with letter.')
    })

    it('the user can close register modal', () => {
        cy.get('.btn-close').click()
        cy.contains('Register new Account').should('not.be.visible')
    })

    it('the user can not register with too short password', () => {
        cy.get('.nav-btn-register').click()
        cy.get('.input-username').type('cyTestUser')
        cy.get('.input-email').type('cy_test_email@trackerrr.com')
        cy.get('.input-password').type('short1')
        cy.get('.input-password2').type('short1')
        cy.get('.btn-register-submit').click()
        cy.contains('Your password must contain at least 8 characters.')
        cy.get('.btn-close').click()
    })

    it('the user can not register with invalid email address', () => {
        cy.get('.nav-btn-register').click()
        cy.get('.input-username').type('cyTestUser')
        cy.get('.input-email').type('cy_test_email@trackerrr')
        cy.get('.input-password').type('test4321')
        cy.get('.input-password2').type('test4321')
        cy.get('.btn-register-submit').click()
        cy.contains('Please enter a valid email address.')
        cy.get('.btn-close').click()
    })

    it('the user can not register with too common password', () => {
        cy.get('.nav-btn-register').click()
        cy.get('.input-username').type('cyTestUser')
        cy.get('.input-email').type('cy_test_email@trackerrr.com')
        cy.get('.input-password').type('12345678')
        cy.get('.input-password2').type('12345678')
        cy.get('.btn-register-submit').click()
        cy.contains('be a commonly used password or similar to your other personal information.')
        cy.get('.btn-close').click()
    })
    

    it('the user can not register with username that is already in use', () => {
        cy.get('.nav-btn-register').click()
        cy.get('.input-username').type('tests')
        cy.get('.input-email').type('cy_test_email@trackerrr.com')
        cy.get('.input-password').type('test4321')
        cy.get('.input-password2').type('test4321')
        cy.get('.btn-register-submit').click()
        cy.contains('Username already taken')
        cy.get('.btn-close').click()
    })

    it('the user can register new account', () => {
        cy.get('.nav-btn-register').click()
        cy.get('.input-username').type('cyTestUser')
        cy.get('.input-email').type('cy_test_email@trackerrr.com')
        cy.get('.input-password').type('test4321')
        cy.get('.input-password2').type('test4321')
        cy.get('.btn-register-submit').click()
        cy.contains('Account has been created')
    })

    
})