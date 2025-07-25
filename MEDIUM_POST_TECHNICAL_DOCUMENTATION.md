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

## 2. Technical Architecture and Design Decisions

### 2.1 System Architecture Overview

Our system follows a microservices-inspired architecture with clear separation
of concerns:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React SPA     │    │  Flask Backend  │    │   MongoDB       │
│   (Frontend)    │◄──►│   Services      │◄──►│   Database      │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
    ┌─────────┐           ┌─────────────┐         ┌─────────────┐
    │   UI    │           │    JWT      │         │  Document   │
    │ Router  │           │    Auth     │         │   Store     │
    └─────────┘           └─────────────┘         └─────────────┘
```

### 2.2 Technology Stack Justification

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

## 3. Development Methodology and Project Management

### 3.1 Iterative Development Approach

Our development followed a structured three-prototype methodology:

#### Prototype 1: Foundation (Weeks 1-4)

**Objectives:** Core authentication and basic user management

- User registration and login system
- Basic profile management
- Database schema design
- Initial React component structure

**Key Achievements:**

- Secure JWT authentication implementation
- MongoDB integration with user collections
- Responsive UI framework establishment
- Development environment standardization

#### Prototype 2: Core Features (Weeks 5-8)

**Objectives:** Lost pet reporting and response system

- Integration with user management module
- Pet loss report creation and management
- Response system for reports
- Image upload and storage

**Key Achievements:**

- File upload service with image processing
- Advanced search and filtering of reports
- Geolocation integration for pet reports
- Advanced form validation

#### Prototype 3: Integration and Enhancement (Weeks 9-12)

**Objectives:** System integration and user experience optimization

- Reputation system for users
- Notification system for report updates
- Educational content management
- Performance optimization

**Key Achievements:**

- Complete educational module with categorized content
- Enhanced notification system with real-time updates
- Improved responsive design
- Comprehensive testing suite

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
