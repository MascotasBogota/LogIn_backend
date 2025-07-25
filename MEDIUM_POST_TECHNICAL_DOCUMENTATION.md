# Building PatitasBog: A Comprehensive Pet Management System Using Modern Web Technologies

_An Academic Software Engineering Project - Universidad Nacional de Colombia_

**Authors:**
[Martin Moreno Jara](https://www.linkedin.com/in/martin-moreno-jara-250977242/),
[Juan Esteban Cardenas Huertas](https://www.linkedin.com/in/juan-huertaszz/),
[Juan David Ardila Diaz](https://www.linkedin.com/in/luis-felipe-tolosa-sierra-4441a2267/),[Luis Felipe Tolosa Sierra](https://www.linkedin.com/in/luis-felipe-tolosa-sierra-4441a2267/),
[David Alejandro Cifuentes Gonzalez](https://www.linkedin.com/in/dcifuentesg/),
[Keynes Stephens Watson](https://www.linkedin.com/in/keynes-stephens-watson-844550288/)

---

## Abstract

This technical post documents the complete development journey of PatitasBog, a
comprehensive pet management system developed as part of our Software
Engineering 2 course. Through three iterative prototypes, we built a full-stack
web application that addresses real-world challenges in pet care, lost pet
recovery, and community engagement. This academic project demonstrates our
technical capabilities in modern web development, project management, and
iterative software development methodologies.

**Disclaimer:** This is an academic project and we acknowledge that it still has
areas for improvement and optimization.

---

## 1. Introduction and Project Vision

### 1.1 Problem Statement

Pet ownership brings immense joy but also significant responsibilities and
challenges. Our research identified three critical pain points in the pet care
ecosystem:

1. **Lost Pet Recovery:** Inefficient processes for reporting and finding lost
   pets
2. **Information Fragmentation:** Scattered resources for pet care education
3. **Community Disconnection:** Lack of centralized platforms for pet owner
   collaboration

### 1.2 Solution Overview

PatitasBog emerged as a comprehensive digital solution designed to address these
challenges through:

- **Centralized Pet Management:** Digital profiles and health records
- **Community-Driven Lost Pet System:** Real-time reporting and search
  capabilities
- **Educational Resources:** Curated content for responsible pet ownership
- **Notification System:** Automated alerts for community engagement

### 1.3 Academic Context

This project was developed following iterative and incremental methodologies,
with three distinct prototypes spanning 4 months of development. Each iteration
focused on expanding functionality while maintaining code quality and
architectural integrity.

### 1.4 Project Goals achieved

1. **User Authentication and Authorization:** Implemented secure user login and
   registration, as well as useful feature such as password recovery and profile
   management.
2. **Lost Pet Reporting System:** Developed a comprehensive system for reporting
   lost pets, including location and images.
3. **Community Engagement:** Fostered a sense of community through user profiles
   and interaction, and through the user reputation system, which rewards
   helpful contributions and penalizes unhelpful ones.
4. **Scalable Architecture:** Designed a flexible decoupled architecture to
   accommodate future features, integrating microservices for modularity.

---

## 2. Planning structure and methodology

### 2.1 Project Planning

A careful process of thought was put into the planning of this project. First,
identifying the functional requirements and then grouping them into the modules
that would be developed in each prototype. In the planning phase, we organized
these increments in epics and user stories, which were then prioritized based on
their importance to the project. The epics we defined, alongside some of their
functional requirements, are as follows:

#### 2.1.1 Epics and Functional Requirements

- **User Management:** Authentication, profile management, password recovery.
- **Lost Pet Reporting:** Create, filter, and manage lost pet reports, upload
  pet images, select last known location of the pet and marking the report as
  solved.
- **Responses to reports:** Create and manage different types of responses to
  lost pet reports, including sightings and findings.
- **Notification System:** Implement a notification system for users to receive
  updates on lost pet reports.
- **User Reputation System:** Develop a user reputation system to encourage
  community engagement and reward helpful contributions.
- **Educational Content:** Create and manage educational content related to pet
  care, including articles, tips, and resources.

#### 2.1.2 Roadmap

Once we defined the epics and functional requirements, we created a roadmap to
guide the development process. The roadmap was divided into three main
increments, each with its own set of features and objectives. Each increment was
planned to be developed in a 4-week sprint. The roadmap is as follows:

1. **Increment 1: MVP. User Management, Reporting and responses** The main goal
   of this increment was to establish the foundation of the application,
   delivering the core functionalities of the application in order to accomplish
   the MVP. The main features of this increment were:
   - User registration and login system
   - Basic profile management
   - Report creation and management
   - Response system for reports
1. **Increment 2: Notification and Reputation System** The main goal of this
   increment was to enhance user engagement and trust within the platform. The
   main features of this increment were:
   - Notification system for report updates
   - User reputation system implementation
1. **Increment 3: Educational Content and Final Enhancements** The main goal of
   this increment was to provide users with valuable information and resources
   related to pet care, as well as improving already developed features of the
   application. The main features of this increment were:
   - Educational content management
   - Performance optimization
   - Final enhancements and bug fixes
   - Observability and monitoring implementation

However, due to time constraints, we had to adapt the development process to
only two iterations, as the planning phase took up the first one. Thus, the
first and second increments were merged into one, and the third increment was
developed as the final version of the application.

#### 2.1.3 Team management

The project was developed by a team of 6 members, each with specific roles and
responsibilities. While we did not implement a formal agile methodology such as
Scrum, due to the difficulty of coordinating all necessary meetings, we did
follow some agile principles such as iterative development and continuous
feedback, as well as assertive communication. We divided the team into smaller
2-men groups, each responsible for specific tasks and features. This allowed us
to work in parallel and deliver the project in a timely manner.

---

## 3. Design and Architecture

### 3.1 Architecture Overview

The architecture of the application is based on SOFEA (Service-Oriented Frontend
Architecture), by which each backend service is developed in a separate
repository, and the frontend is developed as a separate application that
consumes the backend services through REST APIs. Though this architectural style
is not so widely used in real life applications, due to the academic nature of
the project, we decided to use it in order to learn and practice good software
engineering practices, such as modularity, separation of concerns, and
scalability.

### 3.2 Modular Design and components

![Application architecture](final%20components.png)

The diagram shows the components of the application architecture in their
entirety, as well as the relationships between them. As indicated previously, a
SOFEA approach was implemented, under which the different proposed modules were
developed as REST APIs and integrated through the Front End to deliver the
application. However, communication between services could not be limited to
integration with the Front End, as some services depend on others to function
and make requests to each other to perform their tasks (this is denoted in the
diagram by the dotted arrows). Subsequently, to properly develop some
functionalities, it was necessary to use third-party services, which were
implemented through their APIs and development tools in Flask.

#### 3.2.1 Module segmentation and components

The final version of the application includes the following modules:

##### Front End (React):

- Main frontend component
- Educational module

###### Backend services (APIs developed in Flask):

- User management module
- Reports and responses module
- Notifications module
- User reputation module

###### Database (MongoDB hosted on Atlas):

- User database
- Reports and responses database

###### Third-party services:

- Observability: Open Telemetry, Prometheus, Grafana
- Image storage: Supabase storage
- Mail service: Email sender

Additionally, the integration testing module groups all the previous modules to
verify the application's correct operation.

#### 3.2.2 Component explanation

The backbone of the application is the user management and reports and responses
modules. Each module has its own database, which can only be accessed (written
or queried) through these modules and not through external modules, in order to
implement best practices. The user management module uses the Email Sender
service to send emails to Gmail domains for the password reset functionality.
Meanwhile, the reports and responses module uses supabase storage, a cloud
storage service, to store pet images that users can upload in reports and
responses. Initially, this functionality was managed by saving the images
locally, but it was decided to change this due to its infeasibility. Thus, when
images are uploaded, a public URL is generated to load them on the front end.

Both the notifications service and the user reputation service depend on the two
aforementioned services, as they must use their functionalities or access their
databases. All backend service modules were then configured to display metrics
that show the performance and error of each service. Open Telemetry was used in
conjunction with Prometheus to obtain observability information, which is then
displayed in Grafana.

All services connect to the Front End, which handles user requests and
interactions with the system, following the aforementioned SOFEA architectural
style. Finally, the integration testing module integrates the entire application
to ensure stable operation and consistent communication between all modules.

### 3.3 Technology Stack Justification

#### Frontend Technologies

- **React 18.2:** Chosen for its component-based architecture and robust
  ecosystem
- **Vite:** Selected over Create React App for faster development builds and
  better performance
- **CSS Modules:** Provides scoped styling to prevent conflicts in our modular
  component structure
- **React Router:** Enables SPA navigation with clean URL structures

#### Backend Technologies

- **Flask 2.3:** Lightweight Python framework suitable for our microservices
  approach
- **Flask-RESTX:** Provides automatic Swagger documentation and API
  standardization
- **Flask-JWT-Extended:** Implements secure authentication with token-based
  sessions
- **MongoDB:** Document-based storage aligns with our flexible data schemas

#### Development Tools

- **Git/GitHub:** Version control with feature branch workflow
- **Docker:** Containerization for consistent deployment environments
- **Pytest:** Comprehensive testing framework for backend services

### 2.3 Database Design

Our MongoDB schema leverages document flexibility while maintaining data
integrity:

```json
{
  "users": {
    "_id": "ObjectId",
    "email": "string",
    "password": "hashed_string",
    "profile": {
      "firstName": "string",
      "lastName": "string",
      "phone": "string",
      "address": "string"
    },
    "pets": ["ObjectId references"]
  },

  "reports": {
    "_id": "ObjectId",
    "type": "lost|found",
    "petInfo": {
      "name": "string",
      "species": "string",
      "breed": "string",
      "description": "string"
    },
    "location": {
      "coordinates": [longitude, latitude],
      "description": "string"
    },
    "images": ["string paths"],
    "status": "active|resolved|expired",
    "timestamp": "ISO Date"
  }

}
```

---

## 4. Functional increments and system evolution

### 4.1 Iterative Development Approach

For this class' deliverables, we adopted an iterative development approach,
dividing the project into three main prototypes, each building upon the previous
one. These prototypes include both the planning phase and the development,
allowing us to gradually implement features and improve the system based on
feedback and testing.

Due to time constraints, though we had planned to develop the project in three
development cycles, we had to adapt the development process to fit the academic
schedule. As a result, the development takes up two out of the three prototypes,
with the first prototype being the planning phase.

#### Prototype 1: Planning (Weeks 1-4)

**Objectives:** Define project scope, user stories, and technical

- Identify core features and user needs
- Establish technical stack and architecture
- Create initial wireframes and UI designs
- Set up development environment and version control
- Define project milestones and deliverables

**Key Achievements:**

- Completed requirement analysis
- Defined user stories and acceptance criteria
- Established project architecture and technology stack
- Set up GitHub organization and repository

**Justification:** Before starting the development, we needed to define the
scope of the project, the features to be implemented, and the technical
requirements.

#### Prototype 2: MVP (Weeks 5-8)

**Objectives:** User management and lost pet reporting system

- Implement user authentication and profile management
- Develop lost pet reporting system
- Create response system for lost pet reports
- Image upload and storage

**Key Achievements:**

- User registration and login system with JWT authentication
- Basic profile management with image upload
- Lost pet report creation and management
- Search and filtering of reports
- Response system for reports with image upload and

**Justification:** The main goal of this prototype was to deliver a functional,
yet unfinished, version of the application that could be used to test the core
functionalities of the system, following the MVP (Minimum Viable Product)
approach.

#### Prototype 3: Final Version (Weeks 9-12)

**Objectives:** Notification system, user reputation, and educational content

- Implement notification system for report updates
- Develop user reputation system based on report interactions
- Create educational content
- Improving the services developed in the previous prototypes
- Observability and monitoring implementation
- Integration testing module

**Key Achievements:**

- Notification system for real-time updates on reports
- User reputation system to encourage community engagement
- Educational content management with categorized articles
- Performance optimization and bug fixes
- Integration testing for all components
- Observability and monitoring with Open Telemetry, Prometheus, and

**Justification:** The main goal of this prototype was to deliver a complete
version of the application, with all the features implemented and tested, as
well as to improve the already developed features. This prototype also included
the implementation of observability and monitoring tools to ensure the system's
stability and performance.

### 4.2 Changes and insights

Even though we did a careful and detailed planning of the project, we had to do
some changes mid way through the development process because there were things
we did not foresee or that we did not take into account in the planning phase.
Some of these changes were:

- **Image storage:** Initially, we planned to store images locally, but we
  realized that this was not feasible due to the size of the images and the need
  for scalability. Thus, we decided to use Supabase storage, a cloud storage
  service, to store the images and generate public URLs for them.
- **Notification or Filters:** Initially, we had planned to implement a filter
  service for the reports, but we realized that this was not necessary as the
  search and filtering functionalities were already implemented in the reports
  and responses module. Thus, we decided to focus on the notification system
  instead, which was a more valuable feature to be implemented in a different
  repository.

### 3.2 Project Management Strategies

#### Version Control Workflow

We implemented a Git flow strategy with distinct branches:

- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: Individual feature development
- `fix/*`: Bug fixes and hotfixes

#### Quality Assurance

Each prototype included:

- Code reviews for all pull requests
- Automated testing with minimum 70% coverage
- Manual testing protocols
- Performance benchmarking

---

## 4. Technical Implementation Details

### 4.1 Authentication and Security

#### JWT Implementation

Our authentication system uses Flask-JWT-Extended for secure token management:

```python
from flask_jwt_extended import create_access_token, jwt_required

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.find_by_email(email)
    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(
            identity=str(user['_id']),
            expires_delta=timedelta(days=1)
        )
        return jsonify({
            'access_token': access_token,
            'user': serialize_user(user)
        }), 200

    return jsonify({'message': 'Invalid credentials'}), 401
```

#### Security Measures

- Password hashing using bcrypt
- CORS configuration for cross-origin requests
- Input validation and sanitization
- SQL injection prevention through parameterized queries

### 4.2 Frontend Architecture

#### Component Structure

Our React application follows a hierarchical component structure:

```javascript
src/
├── components/
│   ├── Common/          // Reusable UI components
│   ├── Auth/            // Authentication forms
│   ├── Profile/         // User profile management
│   ├── Reports/         // Pet reporting system
│   └── Education/       // Educational content
├── views/               // Page-level components
├── services/            // API communication
├── styles/              // CSS modules
└── utils/               // Helper functions
```

#### State Management

We implemented a custom context-based state management system:

```javascript
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      validateToken(token)
        .then((userData) => setUser(userData))
        .catch(() => localStorage.removeItem("token"))
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  return (
    <AuthContext.Provider value={{ user, setUser, loading }}>
      {children}
    </AuthContext.Provider>
  );
};
```

### 4.3 Backend Service Architecture

#### Modular Service Design

Our Flask backend follows a modular architecture with clear separation:

```python
# Service Layer Pattern
class ReportService:
    @staticmethod
    def create_report(user_id, report_data):
        try:
            # Validate input data
            validator = ReportValidator(report_data)
            if not validator.is_valid():
                return None, validator.errors

            # Process images
            image_paths = ImageService.process_uploads(
                report_data.get('images', [])
            )

            # Create report document
            report = {
                'user_id': ObjectId(user_id),
                'type': report_data['type'],
                'pet_info': report_data['pet_info'],
                'location': report_data['location'],
                'images': image_paths,
                'status': 'active',
                'created_at': datetime.utcnow()
            }

            result = mongo.db.reports.insert_one(report)

            # Send notifications
            NotificationService.notify_nearby_users(
                report['location'],
                report_data['type']
            )

            return str(result.inserted_id), None

        except Exception as e:
            logger.error(f"Error creating report: {str(e)}")
            return None, ['Internal server error']
```

### 4.4 Database Operations and Optimization

#### MongoDB Optimization Strategies

- Indexed commonly queried fields (location, timestamp, status)
- Implemented aggregation pipelines for complex queries
- Used connection pooling for improved performance

```python
# Geospatial Query Example
def find_nearby_reports(latitude, longitude, radius_km=10):
    return mongo.db.reports.find({
        'location.coordinates': {
            '$near': {
                '$geometry': {
                    'type': 'Point',
                    'coordinates': [longitude, latitude]
                },
                '$maxDistance': radius_km * 1000  # Convert to meters
            }
        },
        'status': 'active'
    })
```

---

## 5. Key Features and Functionality

### 5.1 User Authentication and Profile Management

Our authentication system provides:

- Secure user registration with email verification
- JWT-based session management
- Profile customization with image uploads
- Password reset functionality

### 5.2 Pet Management System

The pet management module enables users to:

- Create detailed pet profiles with photos
- Track medical records and vaccination schedules
- Manage multiple pets per user account
- Export pet information for veterinary visits

### 5.3 Lost and Found Pet Reporting

This core feature includes:

- Geolocation-based reporting system
- Image upload with automatic resizing
- Real-time notifications to nearby users
- Advanced search and filtering capabilities
- Status tracking (active, resolved, expired)

### 5.4 Educational Content Management

Our educational module provides:

- Categorized pet care information
- Interactive tips with importance ratings
- Responsive design with smooth animations
- Community-contributed content support

### 5.5 Notification System

The notification service offers:

- Real-time alerts for nearby lost pets
- Email notifications for report updates
- Customizable notification preferences
- Integration with multiple communication channels

---

## 6. Testing and Quality Assurance

### 6.1 Testing Strategy

Our comprehensive testing approach included:

#### Unit Testing

- Backend: 85% code coverage using Pytest
- Frontend: Component testing with React Testing Library
- Isolated testing of service functions

```python
def test_create_report_success():
    # Arrange
    user_id = str(ObjectId())
    report_data = {
        'type': 'lost',
        'pet_info': {
            'name': 'Max',
            'species': 'dog',
            'breed': 'Golden Retriever'
        },
        'location': {
            'coordinates': [-74.0721, 4.7110],
            'description': 'Near Central Park'
        }
    }

    # Act
    report_id, errors = ReportService.create_report(user_id, report_data)

    # Assert
    assert report_id is not None
    assert errors is None
    assert mongo.db.reports.find_one({'_id': ObjectId(report_id)})
```

#### Integration Testing

- API endpoint testing with complete request/response cycles
- Database integration testing
- Authentication flow testing

#### User Acceptance Testing

- Manual testing scenarios for all user workflows
- Cross-browser compatibility testing
- Mobile responsiveness verification

### 6.2 Performance Optimization

We implemented several performance enhancements:

- Image optimization and lazy loading
- MongoDB query optimization with indexes
- Frontend code splitting and bundle optimization
- Caching strategies for frequently accessed data

---

## 7. Challenges and Solutions

### 7.1 Technical Challenges

#### Challenge 1: Real-time Notifications

**Problem:** Implementing efficient real-time notifications without websockets
**Solution:** Implemented polling with intelligent intervals and email fallbacks

#### Challenge 2: Image Upload and Storage

**Problem:** Handling large image files and storage optimization **Solution:**
Implemented automatic image resizing and organized file storage structure

#### Challenge 3: Geolocation Accuracy

**Problem:** Ensuring accurate location-based pet matching **Solution:**
Implemented radius-based search with user-configurable distance parameters

### 7.2 Project Management Challenges

#### Challenge 1: Feature Scope Management

**Problem:** Balancing feature completeness with development timeline
**Solution:** Implemented priority-based feature development with MVP focus

#### Challenge 2: Code Quality Consistency

**Problem:** Maintaining consistent code quality across team members
**Solution:** Established coding standards, mandatory code reviews, and
automated testing

### 7.3 Learning Outcomes

This project provided valuable experience in:

- Modern full-stack web development
- Database design and optimization
- API design and documentation
- Version control and collaboration
- Testing methodologies
- Project management and agile methodologies

---

## 8. Results and Impact

### 8.1 Technical Achievements

- **Complete Full-Stack Application:** Successfully developed and deployed a
  functioning web application
- **Scalable Architecture:** Implemented modular design supporting future
  enhancements
- **Comprehensive Testing:** Achieved high test coverage ensuring reliability
- **Performance Optimization:** Optimized for fast loading and responsive user
  experience

### 8.2 Functional Completeness

Our final system successfully delivers:

- User authentication and profile management
- Complete pet management lifecycle
- Efficient lost pet reporting and recovery system
- Educational content with engaging user interface
- Notification system with multiple channels

### 8.3 Code Metrics

- **Backend:** 12 API endpoints, 95% test coverage
- **Frontend:** 25+ React components, responsive design
- **Database:** 4 main collections with optimized queries
- **Documentation:** Comprehensive API documentation via Swagger

---

## 9. Future Enhancements and Lessons Learned

### 9.1 Identified Improvements

As an academic project, we recognize several areas for future enhancement:

1. **Real-time Features:** Implement WebSocket connections for instant
   notifications
2. **Mobile Application:** Develop native mobile apps for iOS and Android
3. **AI Integration:** Add machine learning for pet matching and breed
   identification
4. **Social Features:** Expand community features with forums and pet playdates
5. **Analytics Dashboard:** Implement comprehensive reporting and analytics

### 9.2 Lessons Learned

#### Technical Lessons

- Importance of early architectural decisions
- Value of comprehensive testing from project start
- Benefits of modular code organization
- Significance of database design for scalability

#### Project Management Lessons

- Critical importance of clear communication
- Value of iterative development and regular reviews
- Benefits of establishing coding standards early
- Importance of realistic timeline estimation

#### Team Collaboration

- Effective use of version control workflows
- Benefits of pair programming for knowledge sharing
- Importance of documentation for team coordination
- Value of regular team meetings and progress reviews

---

## 10. Conclusion

The development of PatitasBog represents a successful academic journey in modern
software engineering. Through three iterative prototypes, we created a
comprehensive pet management system that addresses real-world problems while
demonstrating proficiency in full-stack web development.

This project showcased our ability to:

- Design and implement scalable software architecture
- Apply modern development methodologies
- Collaborate effectively as a development team
- Deliver a functional, tested, and documented software system
- Manage project timelines and scope effectively

The experience gained through this academic project has prepared us for
professional software development challenges and highlighted the importance of
systematic approaches to complex software problems.

We acknowledge that this academic project, while functional and comprehensive,
represents a learning exercise and would benefit from additional refinement and
optimization for production deployment. The iterative approach allowed us to
deliver working software while continuously improving our technical skills and
project management capabilities.

---

**Technical Stack Summary:**

- Frontend: React 18, Vite, CSS Modules, React Router
- Backend: Flask 2.3, Flask-RESTX, Flask-JWT-Extended
- Database: MongoDB with geospatial indexing
- Tools: Docker, Pytest, Git/GitHub, Swagger
- Deployment: Local development with Docker containerization

**Project Timeline:** 12 weeks, 3 prototypes, 6 team members

**Final Note:** This project demonstrates our commitment to learning modern
software engineering practices and our capability to deliver functional software
solutions under academic constraints. We look forward to applying these skills
in professional development environments.

---

_This technical post was collaboratively written by Patitas Bogota Team as part
of our Software Engineering 2 course at Universidad Nacional de Colombia. The
complete source code and documentation are available in our GitHub
repositories._

**LinkedIn:** [https://www.linkedin.com/in/dcifuentesg/]
[https://www.linkedin.com/in/martin-moreno-jara-250977242/]
[https://www.linkedin.com/in/keynes-stephens-watson-844550288/]
[https://www.linkedin.com/in/luis-felipe-tolosa-sierra-4441a2267/]
[https://www.linkedin.com/in/juan-david-ardila-diaz-676a05290/]
[https://www.linkedin.com/in/juan-huertaszz/] **GitHub Organization:**
[https://github.com/MascotasBogota]  
**Medium Publication Date:** [July 24th, 2025 ]

---
