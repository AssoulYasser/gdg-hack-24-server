# gdg-hack-24-server

1. **Occupation**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | name | String | Primary Key, Max Length: 50 |

2. **Deliverables**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | name | String | Primary Key, Max Length: 50 |

3. **Feedback**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | rating | Integer | Choices: 1 to 5 |
   | comment | Text |  |

4. **Profile**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | email | String | Primary Key, Email Format |
   | password | String | Max Length: 256 |
   | first_name | String | Max Length: 20 |
   | last_name | String | Max Length: 20 |
   | discord_id | String | Unique, Nullable, Max Length: 32 |
   | phone_number | String | Unique, Max Length: 10 |
   | created | DateTime | Auto-set on creation |
   | is_occupied | Boolean | Default: False |

5. **Admin**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | profile | Foreign Key | References Profile, On Delete: Protect |

6. **Event**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | id | String | Primary Key, Max Length: 20 |
   | name | String | Max Length: 20 |
   | start_date_time | DateTime |  |
   | end_date_time | DateTime |  |
   | submissions_deadline | DateTime |  |
   | leader | Foreign Key | References Profile, On Delete: Protect |
   | judge_password | String | Max Length: 256 |
   | created | DateTime | Auto-set on creation |

7. **Participant**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | profile | Foreign Key | References Profile, On Delete: Cascade |
   | event | Foreign Key | References Event, On Delete: Cascade |
   | occupation | Foreign Key | References Occupation, On Delete: Cascade |
   | is_team_leader | Boolean | Default: False |
   | team_name | String | Nullable, Max Length: 50 |
   | joined | DateTime | Auto-set on join |

8. **Submission**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | id | String | Primary Key, Max Length: 20 |
   | participant | Foreign Key | References Participant, On Delete: Cascade |
   | event | Foreign Key | References Event, On Delete: Cascade |
   | deliverable | Foreign Key | References Deliverable, On Delete: Cascade |
   | submitted_file | File |  |
   | submitted | DateTime | Auto-set on submission |
   | feedback | Foreign Key | References Feedback, Nullable, On Delete: Set Null |

9. **Judge**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | profile | Foreign Key | References Profile, On Delete: Cascade |
   | event | Foreign Key | References Event, On Delete: Cascade |

10. **Notification**
    | Field Name | Data Type | Constraints |
    | --- | --- | --- |
    | id | Integer | Primary Key, Auto-increment |
    | recipient | Foreign Key | References Profile, On Delete: Cascade |
    | message | Text |  |
    | sent | DateTime | Auto-set on creation |
    | is_read | Boolean | Default: False |

11. **ChatMessage**
    | Field Name | Data Type | Constraints |
    | --- | --- | --- |
    | id | Integer | Primary Key, Auto-increment |
    | sender | Foreign Key | References Profile, On Delete: Cascade |
    | recipient | Foreign Key | References Profile, On Delete: Cascade |
    | message | Text |  |
    | sent | DateTime | Auto-set on creation |
    | is_read | Boolean | Default: False |
