# API Reference for Totem AI

## Endpoints:
### `/generate`
- **Description**: Generate a new avatar.
- **Method**: POST
- **Parameters**:
  - `theme`: The theme for the avatar (e.g., fantasy, futuristic).
  - `style`: The style for the avatar (e.g., pixel art, watercolor).

### `/style-transfer`
- **Description**: Apply a style transfer to an avatar.
- **Method**: POST
- **Parameters**:
  - `avatar_id`: ID of the avatar to modify.
  - `style`: Desired style for transformation.
