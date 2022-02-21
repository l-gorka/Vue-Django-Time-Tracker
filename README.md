# Vue-Django-Time-Tracker

## TODO

- [x] Add registration page.
- [x] Add cookie to save started time entry.
- [x] Add colored text in projects dropdown.
- [x] Add delete TimeEntry funcionality.
- [x] Add continue activity funcionality
- [x] Add change date feature to TimeEntry
- [x] 

## Changelog

### 0.1

#### Created TimeEntry component with funcionality listed below:

+ Description field 
+ Projects dropdown allows to choose from existing projects, search for project or create new. Project titles are displayed in colors upon user's choice.
+ Time input fields - display start and end time in format HH:MM. User can manually adjust time, which is saved on @blur event. Input is validated, and if user types incorrect data, the previous value is restored from temporary variable. Before saving, the time is converted to Unix timestamp. In case when timeStart > timeEnd, the timeEnd date passes to the next day.
+ Duration dropdown - displays duration of TimeEntry in format HH:MM:SS. User can manually adjust duration which will be added to startTime. If invalid, input is restored from temporary variable.
+ Play button - starts new TimeEnry, with same Project and description.
+ Options button - allows to duplicate or delete TimeEntry.
+ Toast - pops up when user do some changes.
