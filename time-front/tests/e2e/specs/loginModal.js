// https://docs.cypress.io/api/introduction/api.html

describe('Login modal test', () => {
  it('user can open login modal', () => {
    cy.visit('/')
    cy.contains('h1', 'Time tracker')    
    cy.get('.nav-btn-login').click()
    cy.contains('Log In')
  })

  it('user can not login with empty inputs', () => {
    cy.get('.btn-login-submit').click()
    cy.contains('.help', 'Enter username and password')
  })

  it('user can not login with incorrect password', () => {
    cy.get('.input-username').type('neko4')
    cy.get('.input-password').type('wrong_password123')
    cy.get('.btn-login-submit').click()
    cy.contains('.help', 'Either username or password is incorrect. Please retype your credentials.')
    cy.get('.btn-close').click()
  })

  it('user can login', () => {
    cy.get('.nav-btn-login').click()
    cy.get('.input-username').type('tests')
    cy.get('.input-password').type('test4321')
    cy.get('.btn-login-submit').click()
    cy.url().should('include', 'tracker')
  })
})
