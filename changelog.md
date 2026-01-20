# Changelog

All notable changes to this project will be documented in this file.

## 1.0.3

### Added

#### Location Interface Support
- Added comprehensive ModemManager Location interface support
- New `interfaces_location.py` module with complete location services functionality
- Added location-related enums: `MMModemLocationSource`, `MMModemLocationAssistanceDataType`
- New example file `example/location.py` demonstrating location features
- Support for multiple location sources: GPS, 3GPP, CDMA, etc.
- Location source mapping and property helpers
- Contributors: Kevin Barrios (@barrioskevin)

#### Time Interface Support
- New `interfaces_time.py` module
- Added NetworkTime functionality for network time synchronization
- Contributor: Kim Forest (@kimfor)

#### Simple Interface Enhancements
- New `interfaces_simple.py` module with expanded functionality
- Added additional properties support
- Contributor: Kim Forest (@kimfor)

#### 3GPP Interface Enhancements
- Extended `interfaces_3gpp.py` with additional 3GPP-specific features
- Contributor: Kim Forest (@kimfor)

#### Code Quality
- Added YAPF formatting instructions to README
- Applied YAPF formatting across multiple files for consistent code style

### Fixed

#### SMS Message Management
- Fixed `messaging.delete_sms` function (PR #17)
  - Corrected attribute name from `_sdbus` to `_dbus` (PR #22)
  - Contributor: dazfitzg, copilot-swe-agent[bot]

#### SIM Object Path Validation
- Fixed SIM object path check to ensure valid SIM assignment
- Prevents issues with invalid SIM object paths

#### Location Examples
- Added instructions for enabling location signals in `location.py` example

### Changed

#### Dependency Management
- Migrated from Pipfile to Poetry for dependency management
- Removed `Pipfile` and `Pipfile.lock` (726 lines removed)
- Added `poetry.lock` for reproducible builds

#### Code Organization
- Refactored location-related code for better maintainability
- Improved property return types for location interfaces
- Enhanced enum support for location and assistance data types

### Statistics

- **Files Changed**: 17
- **Insertions**: ~781 lines
- **Deletions**: ~830 lines (primarily from Pipfile.lock removal)
- **Pull Requests**: 3 merged (#17, #19, #20, #22)
- **Contributors**: Kevin Barrios, Kim Forest, dazfitzg, Zhang LongQi

### Key Contributors

- **Kevin Barrios** (@barrioskevin) - Location interface implementation
- **Kim Forest** (@kimfor) - Time and Simple interface support
- **dazfitzg** - SMS deletion fix
- **Zhang LongQi** (@zhanglongqi) - Project maintenance and code review
- **copilot-swe-agent[bot]** - Automated bug fixes
