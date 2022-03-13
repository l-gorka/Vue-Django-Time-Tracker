

describe('TimeTracker tests', () => {

    it('the user can log in', () => {
        cy.visit('/');
        cy.contains('h1', 'Time tracker');
        cy.get('.is-light').click();
        cy.get(':nth-child(1) > .control > .input').type('tests');
        cy.get(':nth-child(2) > .control > .input').type('test4321');
        cy.get('.modal-card-foot').contains('Login').click();
    });

    it('the user can create a project', () => {
        cy.get('.current-task').contains('Project').click();

        cy.get('.is-active > .dropdown-menu > .dropdown-content > .create-project-btn').click();
        cy.get('.column > :nth-child(1) > .control > .input').type('Test_project12');
        cy.get('[aria-label="#1CA085"]').click();
        cy.get('.modal-card-foot > .is-primary').click();
        cy.get('.current-task').contains('Test_project12')
    });

    it('the user can start counter', () => {
        cy.get('.tooltip-btn-counter').contains('START').click()
        cy.get('.counter').contains('00:00:01')
    })

    it('the user can stop counter', () => {
        cy.get('.current-task').contains('STOP').click()
        //cy.get(':nth-child(1) > .panel > .panel-heading').contains('00:00:01')
    })

    it('the user can change Time entry start_date and end_date', () => {
        cy.get('.day-entry-0 > .panel > .panel-body > .time-entry-0 > :nth-child(3) > .control > #input').type('1232')
        cy.get(':nth-child(1) > .panel > .panel-body > :nth-child(1) > :nth-child(4) > .control > #input').type('1332').blur()
    })


    it('the user can delete time entry', () => {
        cy.get('.time-entry-0 > .level > :nth-child(2) > .tooltip-trigger > .button > :nth-child(1) > .icon > .mdi').click()
        cy.get('.is-danger').click()
    })

});