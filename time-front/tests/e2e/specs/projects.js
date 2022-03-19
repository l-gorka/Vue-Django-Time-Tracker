// before runnning any of tests, execute: python3 manage.py testserver test_data
// to load test data


describe('Projects tests', () => {
    it('projects page is accessible for the user', () => {
        cy.visit('/');
        cy.contains('h1', 'Time tracker');
        cy.get('.nav-btn-login').click();
        cy.get('.input-username').type('cyTestData');
        cy.get('.input-password').type('test4321');
        cy.get('.btn-login-submit').click();
        cy.url().should('include', 'tracker');
        cy.get('[href="/projects"]').click()
    });

    it('projects are visible and selectable for the user', () => {
        cy.get('.cy-panel-select-project').contains('Coding').click()
        cy.get('.cy-selected-project').should('contain', 'Coding')
    })

    it('projects total time & num of entries are visible for the user', () => {
        cy.get('.cy-box-total-entries').should('contain', '2')
        cy.get('.cy-box-total-time').should('contain', '01:41:03')
    })

    it('project title and color can be updated by the user', () => {
        cy.get('.cy-btn-edit').click();
        cy.get('.modal-card-title').should('contain', 'Update project')
    })
})