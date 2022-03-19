// before runnning any of tests, execute: python3 manage.py testserver test_data
// to load test data


describe('Dashboard tests', () => {

    it('the user can log in and navigate to dashboard', () => {
        cy.visit('/');
        cy.contains('h1', 'Time tracker');
        cy.get('.nav-btn-login').click();
        cy.get('.input-username').type('cyTestData');
        cy.get('.input-password').type('test4321');
        cy.get('.btn-login-submit').click();
        cy.url().should('include', 'tracker');
        cy.get('[href="/dashboard"]').click()
    });

    it('the user can see total time this week', () => {
        cy.get('.box-time-total').should('contain', 'This week')
        cy.get('.box-time-total').should('contain', '02:13:01')
    })

    it('the user can see this week s top project', () => {
        cy.get('.box-top-project').should('contain', 'Eating')
    })

    it('the user can adjust displayed data to "Last week"', () => {
        cy.get('.cy-date-picker').click()
        cy.get('.cy-date-options').contains('Last week').click()
        cy.get('.box-time-total').should('contain', 'Last week')
        cy.get('.box-time-total').should('contain', '23:59:00')
        cy.get('.box-top-project').should('contain', 'Sleeping')
    })

})