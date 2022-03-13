// https://docs.cypress.io/api/introduction/api.html

describe('Login modal test', () => {
  it('user can open login modal', () => {
    cy.visit('/')
    cy.contains('h1', 'Time tracker')    
    cy.get('.is-light').click()
    cy.contains('Log In')
  })

  it('user can not login with empty inputs', () => {
    cy.get('.btn-submit').click()
    cy.contains('.help', 'Enter username and password')
  })

  it('user can not login with incorrect password', () => {
    cy.get(':nth-child(1) > .control > .input').type('neko4')
    cy.get(':nth-child(2) > .control > .input').type('wrong_password123')
    cy.get('.btn-submit').click()
    cy.contains('.help', 'Either username or password is incorrect. Please retype your credentials.')
    cy.get('.btn-close > span').click()
  })

  it('user can login', () => {
    cy.get('.is-light').click()
    cy.get(':nth-child(1) > .control > .input').type('neko4')
    cy.get(':nth-child(2) > .control > .input').type('test4321')
    cy.get('.modal-card-foot').contains('Login').click()
  })
})
