describe('TimeTracker tests.', () => {

    it('the user can log in', () => {
        cy.visit('/');
        cy.contains('h1', 'Time tracker');
        cy.get('.nav-btn-login').click();
        cy.get('.input-username').type('tests');
        cy.get('.input-password').type('test4321');
        cy.get('.btn-login-submit').click();
        cy.url().should('include', 'tracker');
    });

    it('the user can create a project', () => {
        cy.get('.current-task').contains('Project').click();
        cy.get('.is-active .btn-open-project-modal').click();
        cy.get('.input-title').type('Test_project12');
        cy.get('[aria-label="#1CA085"]').click();
        cy.get('.modal-card-foot .btn-create-project').click();
        cy.get('.current-task').contains('Test_project12');
    });

    it('the user can start counter', () => {
        cy.get('.tooltip-btn-counter').contains('START').click();
        cy.get('.counter').contains('00:00:01');
    });



    it('the user can stop counter', () => {
        cy.get('.current-task').contains('STOP').click();
        cy.get(':nth-child(1) > .panel > .panel-heading').contains('00:00:01');
    });



    it('the user can change Time entry start_date', () => {
        cy.get('.day-entry-0 .time-entry-0').find('.time-input-start > #input').type('0032').blur();

    });

    it('the user can change Time entry end_date', () => {
        cy.wait(200);
        cy.get('.day-entry-0 .time-entry-0').find('.time-input-end > #input').type('0132').blur();

    });

    it('the user can continue timer for activity', () => {
        cy.wait(200);
        cy.get('.day-entry-0 .time-entry-0 .mdi-play-circle').click();
        cy.get('.counter').contains('00:00:01');
        cy.get('.current-task').contains('STOP').click();
        cy.get('.day-entry-0 .panel > .panel-heading').contains('01:00:02');

    });


    it('the user can delete time entry', () => {
        cy.get('.day-entry-0 .time-entry-0 .mdi-delete').click();
        cy.get('.is-danger').click();
        cy.get('.day-entry-0 .panel > .panel-heading').contains('00:00:01');
    });

    it('the user can create and change project of time enry',() => {
        cy.get('.day-entry-0 .time-entry-0').contains('Test_project12').click();
        cy.get('.is-active .btn-open-project-modal').click()
        cy.get('.input-title').type('New_project121');
        cy.get('[aria-label="#2ECC70"]').click();
        cy.get('.modal-card-foot .btn-create-project').click();
        cy.get('.day-entry-0 .time-entry-0').contains('New_project121');
    })


});