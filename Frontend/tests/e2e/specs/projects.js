// before runnning any of tests, execute: python3 manage.py testserver test_data
// to load fixtures


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
        cy.get('#projects-menu').find('.cy-project-colored').should('have.length', 3)
        cy.get('.cy-panel-select-project').contains('Coding').click()
        cy.get('.cy-selected-project').should('contain', 'Coding')
    })

    it('projects total time & num of entries are visible for the user', () => {
        cy.get('.cy-box-total-entries').should('contain', '2')
        cy.get('.cy-box-total-time').should('contain', '01:41:03')
    })

    it('new project can be created by the user', () => {
        cy.get('.cy-panel-select-project').contains('Create').click()
        cy.get('.modal-card-title').should('contain', 'Create new project')
        cy.get('.input-title').type('Fresh project')
        cy.get('[aria-label="#27AF60"]').click()
        cy.get('.btn-create-project').click()

        cy.get('.cy-panel-select-project').contains('Fresh project').find('.cy-project-colored')
        .should('have.css', 'color', 'rgb(39, 175, 96)')

        cy.get('.cy-selected-project').should('contain', 'Fresh project')
        cy.get('body')
    } )

    it('project title and color can be updated by the user', () => {
        cy.get('.cy-btn-edit').click();
        cy.get('.modal-card-title').should('contain', 'Update project')
        cy.get('.input-title').type('{selectall}{backspace}').type('Updated fresh')
        cy.get('[aria-label="#F2C511"]').click()
        cy.get('.btn-create-project').click()

        cy.get('.cy-panel-select-project').contains('Updated fresh').find('.cy-project-colored')
        .should('have.css', 'color', 'rgb(242, 197, 17)')
        cy.get('.cy-selected-project').should('contain', 'Updated fresh')
    })

    it('the user can search for a project', () => {
        cy.get('.cy-input-search').type('frESH')
        cy.get('#projects-menu').find('.cy-project-colored').should('have.length', 1)
        cy.get('.cy-panel-select-project').should('not.contain', 'Coding')
        cy.get('.cy-panel-select-project').should('not.contain', 'Sleeping')
        cy.get('.cy-panel-select-project').should('contain', 'Updated fresh')
        cy.get('.cy-input-search').type('{selectall}{backspace}')
        cy.get('.cy-panel-select-project').should('contain', 'Coding')
    })

    it('the user can delete project', () => {
        cy.get('#projects-menu').find('.cy-project-colored').should('have.length', 4)
        cy.get('.cy-btn-delete').click();
        cy.get('.is-danger').click()
        cy.get('#projects-menu').find('.cy-project-colored').should('have.length', 3)
        cy.get('.cy-panel-select-project').should('not.contain', 'Updated fresh')
    })
})