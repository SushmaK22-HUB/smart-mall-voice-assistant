---
name: Obsidian Pulse
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#ffb68d'
  on-secondary: '#532200'
  secondary-container: '#e3701e'
  on-secondary-container: '#491d00'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#9a9898'
  on-tertiary-container: '#313131'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#ffdbc9'
  secondary-fixed-dim: '#ffb68d'
  on-secondary-fixed: '#331200'
  on-secondary-fixed-variant: '#763300'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding-mobile: 20px
  container-padding-desktop: 48px
  gutter: 24px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The design system is engineered for a premium Smart Mall Voice Assistant, targeting high-end shoppers who value efficiency and luxury. The aesthetic is "Obsidian Glass"—a sophisticated fusion of deep, dark surfaces and luminous accents.

The personality is authoritative yet welcoming, utilizing a **Glassmorphism** style to create depth without clutter. The UI should evoke a sense of being in a high-tech, exclusive lounge. Key characteristics include:
- **Depth through Translucency:** Interfaces feel like suspended panes of dark glass.
- **Luminous Interaction:** Interactions are signaled by vibrant orange glows, simulating light passing through glass.
- **Precision:** Ultra-thin borders and generous whitespace reflect a boutique shopping experience.

## Colors

The palette is anchored in **Obsidian (#0F0F0F)** for the base background to ensure maximum contrast and a "true black" premium feel on OLED displays. 

- **Primary & Secondary:** Vibrant Orange shades serve as the "voice pulse" and primary action triggers. They represent energy and high-visibility assistance.
- **Surface Tiers:** Deep charcoal (#1A1A1A) is used for card backgrounds. 
- **Glass Effects:** Use the `glass_fill` and `glass_border` for all container elements. The border should be a constant 1px stroke to define edges against the dark background.

## Typography

This design system utilizes **Inter** for its systematic, clean, and highly legible characteristics. In a dark-themed voice assistant, clarity is paramount.

- **Headlines:** Use Bold and Semi-Bold weights with slight negative letter-spacing to create a "locked-in" professional look.
- **Voice Response:** Large, clear body text is essential for glanceable information while walking. 
- **Labels:** Uppercase labels with increased letter-spacing are used for categorization and technical metadata (e.g., "FLOOR 2", "OPEN UNTIL 10PM").

## Layout & Spacing

The layout follows a **Fluid Grid** approach with a focus on safe tap targets and generous margins to prevent visual noise.

- **Rhythm:** An 8px base unit governs all dimensions.
- **Safe Areas:** On mobile/kiosk, maintain a 20px minimum margin from the edge to account for bezel shadows.
- **Voice-First Design:** The bottom 30% of the screen is reserved for the voice visualizer and primary interaction controls, ensuring easy accessibility for thumb or hand interaction.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** rather than traditional drop shadows.

1.  **Level 0 (Base):** Deep Obsidian (#0F0F0F) background.
2.  **Level 1 (Cards):** Translucent fill (rgba 26, 26, 26, 60%) with a 20px backdrop blur and 1px border.
3.  **Level 2 (Active States):** Increased border opacity (rgba 255, 255, 255, 20%) and a subtle #FF6B00 outer glow (15px blur, 10% opacity) to indicate the active listening state or a selected item.

## Shapes

The shape language is "Substantial Softness." Using **Rounded (Level 2)** settings ensures that the UI feels approachable and modern, moving away from the harshness of sharp corners common in older enterprise systems.

- **Standard Elements:** 0.5rem (8px) for buttons and inputs.
- **Large Containers:** 1.5rem (24px) for main mall maps or category cards to create a distinctive silhouette.

## Components

### Buttons
- **Primary:** Solid #FF6B00 with white text. High-elevation buttons feature a soft orange drop-shadow/glow to simulate light emission.
- **Glass Button:** Transparent background, 1px white (10% opacity) border, used for secondary mall navigation.

### Cards
- All cards use `backdrop-filter: blur(20px)`.
- Cards for "Store Listings" should include a subtle gradient overlay from bottom to top to ensure text legibility over store photography.

### Voice Visualizer
- A dynamic, fluid wave component. When the user speaks, the wave pulses between #FF6B00 and #FF8533. 

### Inputs & Selection
- **Checkboxes/Radios:** Use the primary orange for the "on" state.
- **Input Fields:** Darker than the card background (#0A0A0A) with a thin orange focus ring.

### Refined Iconography
- Use thin-stroke (1.5px) icons. Avoid solid fills unless the icon is in an "active" or "selected" state, where it should transition to the primary orange.