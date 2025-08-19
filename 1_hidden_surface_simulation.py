import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.animation as animation
import time


class HiddenSurfaceSimulation:
    def __init__(self):
        self.surfaces = []
        self.visible_surfaces = []
        self.angle = 0

    def add_surface(self, vertices, color='blue', name='Surface'):
        """Add a surface defined by vertices"""
        vertices_array = np.array(vertices)
        surface = {
            'vertices': vertices_array,
            'color': color,
            'name': name,
            'normal': self.calculate_normal(vertices),
            'center': np.mean(vertices_array, axis=0)
        }
        self.surfaces.append(surface)

    def calculate_normal(self, vertices):
        """Calculate surface normal using cross product"""
        vertices = np.array(vertices)
        v1 = vertices[1] - vertices[0]
        v2 = vertices[2] - vertices[0]
        normal = np.cross(v1, v2)
        norm = np.linalg.norm(normal)
        if norm != 0:
            normal = normal / norm
        return normal

    def get_camera_position(self, angle, radius=8):
        """Calculate camera position based on angle"""
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        z = 6
        return np.array([x, y, z])

    def back_face_culling(self, view_point):
        """Remove back-facing surfaces"""
        visible = []
        culled = []

        for surface in self.surfaces:
            view_vector = view_point - surface['center']
            view_vector = view_vector / np.linalg.norm(view_vector)
            dot_product = np.dot(surface['normal'], view_vector)

            if dot_product > 0.1:  # Small threshold for stability
                visible.append(surface)
            else:
                culled.append(surface)

        self.visible_surfaces = visible
        return visible, culled

    def z_buffer_sort(self, view_point):
        """Sort surfaces by distance from viewer"""
        for surface in self.visible_surfaces:
            distance = np.linalg.norm(view_point - surface['center'])
            surface['distance'] = distance

        self.visible_surfaces.sort(key=lambda x: x['distance'], reverse=True)


class CubeSimulation(HiddenSurfaceSimulation):
    def __init__(self):
        super().__init__()
        self.create_cube()

    def create_cube(self):
        """Create cube surfaces"""
        size = 2
        vertices = [
            [-size, -size, -size], [size, -size, -size], [size,
                                                          size, -size], [-size, size, -size],
            [-size, -size, size],  [size, -size, size],  [size,
                                                          size, size],  [-size, size, size]
        ]

        faces = [
            ([0, 1, 2, 3], 'red', 'Bottom'),
            ([4, 7, 6, 5], 'blue', 'Top'),
            ([0, 4, 5, 1], 'green', 'Front'),
            ([2, 6, 7, 3], 'yellow', 'Back'),
            ([1, 5, 6, 2], 'cyan', 'Right'),
            ([0, 3, 7, 4], 'magenta', 'Left')
        ]

        for face_indices, color, name in faces:
            face_vertices = [vertices[i] for i in face_indices]
            self.add_surface(face_vertices, color, name)


def animate_hidden_surface_elimination():
    """Main animation function"""
    # Create simulation
    sim = CubeSimulation()

    # Set up the figure and 3D axis
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Style the plot
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('white')
    ax.yaxis.pane.set_edgecolor('white')
    ax.zaxis.pane.set_edgecolor('white')
    ax.xaxis.pane.set_alpha(0.1)
    ax.yaxis.pane.set_alpha(0.1)
    ax.zaxis.pane.set_alpha(0.1)

    # Set labels
    ax.set_xlabel('X', color='white')
    ax.set_ylabel('Y', color='white')
    ax.set_zlabel('Z', color='white')

    # Set limits
    limit = 5
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_zlim([-limit, limit])

    # Animation function
    def update(frame):
        ax.clear()

        # Reset style after clear
        ax.set_facecolor('black')
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_edgecolor('white')
        ax.yaxis.pane.set_edgecolor('white')
        ax.zaxis.pane.set_edgecolor('white')
        ax.xaxis.pane.set_alpha(0.1)
        ax.yaxis.pane.set_alpha(0.1)
        ax.zaxis.pane.set_alpha(0.1)

        # Calculate camera position
        angle = frame * 0.1
        camera_pos = sim.get_camera_position(angle)

        # Perform hidden surface elimination
        visible, culled = sim.back_face_culling(camera_pos)
        sim.z_buffer_sort(camera_pos)

        # Draw visible surfaces
        for surface in sim.visible_surfaces:
            vertices = surface['vertices']
            poly = [[vertices[j] for j in range(len(vertices))]]
            collection = Poly3DCollection(poly, alpha=0.8)
            collection.set_facecolor(surface['color'])
            collection.set_edgecolor('white')
            collection.set_linewidth(2)
            ax.add_collection3d(collection)

        # Draw camera position
        ax.scatter([camera_pos[0]], [camera_pos[1]], [camera_pos[2]],
                   color='red', s=100, marker='o')

        # Add title with information
        visible_names = [s['name'] for s in visible]
        culled_names = [s['name'] for s in culled]

        title = f'Hidden Surface Elimination Simulation\n'
        title += f'Camera: ({camera_pos[0]:.1f}, {camera_pos[1]:.1f}, {camera_pos[2]:.1f})\n'
        title += f'Visible: {len(visible)}/6 - {", ".join(visible_names)}\n'
        title += f'Culled: {", ".join(culled_names)}'

        ax.set_title(title, color='white', fontsize=12)
        ax.set_xlabel('X', color='white')
        ax.set_ylabel('Y', color='white')
        ax.set_zlabel('Z', color='white')
        ax.set_xlim([-limit, limit])
        ax.set_ylim([-limit, limit])
        ax.set_zlim([-limit, limit])

        # Print to console
        if frame % 20 == 0:  # Print every 20 frames
            print(
                f"Frame {frame}: Angle={angle:.2f}, Visible={len(visible)}, Culled={len(culled)}")
            for i, surface in enumerate(sim.visible_surfaces):
                print(
                    f"  {i+1}. {surface['name']} (distance: {surface['distance']:.2f})")

    # Create and run animation
    print("Starting Hidden Surface Elimination Simulation...")
    print("The camera will rotate around the cube showing which faces are visible.")
    print("Red dot = Camera position")
    print("Colored faces = Visible surfaces (after back-face culling)")
    print("Missing faces = Culled surfaces (facing away from camera)")
    print("\nPress Ctrl+C to stop the simulation.\n")

    anim = animation.FuncAnimation(
        fig, update, frames=200, interval=100, repeat=True)

    try:
        plt.show()
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

    return anim


def static_demo():
    """Show static views from different angles"""
    sim = CubeSimulation()

    angles = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4]
    fig, axes = plt.subplots(2, 3, figsize=(
        18, 12), subplot_kw={'projection': '3d'})
    fig.patch.set_facecolor('black')

    for i, angle in enumerate(angles):
        ax = axes[i//3, i % 3]
        ax.set_facecolor('black')

        # Get camera position
        camera_pos = sim.get_camera_position(angle)

        # Apply hidden surface elimination
        visible, culled = sim.back_face_culling(camera_pos)
        sim.z_buffer_sort(camera_pos)

        # Draw surfaces
        for surface in sim.visible_surfaces:
            vertices = surface['vertices']
            poly = [[vertices[j] for j in range(len(vertices))]]
            collection = Poly3DCollection(poly, alpha=0.8)
            collection.set_facecolor(surface['color'])
            collection.set_edgecolor('white')
            collection.set_linewidth(1)
            ax.add_collection3d(collection)

        # Draw camera
        ax.scatter([camera_pos[0]], [camera_pos[1]], [camera_pos[2]],
                   color='red', s=50, marker='o')

        # Style
        ax.set_xlim([-3, 3])
        ax.set_ylim([-3, 3])
        ax.set_zlim([-3, 3])
        ax.set_title(
            f'Angle: {angle:.2f}π\nVisible: {len(visible)}/6', color='white')

        # Style panes
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_alpha(0.1)
        ax.yaxis.pane.set_alpha(0.1)
        ax.zaxis.pane.set_alpha(0.1)

    plt.tight_layout()
    plt.show()


def main():
    """Main function"""
    print("=== Hidden Surface Elimination Simulation ===\n")
    print("Choose simulation type:")
    print("1. Animated Simulation (rotating camera)")
    print("2. Static Views (6 different angles)")

    try:
        choice = input("Enter choice (1 or 2): ").strip()

        if choice == '1':
            animate_hidden_surface_elimination()
        else:
            static_demo()
    except KeyboardInterrupt:
        print("\nSimulation stopped.")


if __name__ == "__main__":
    main()

"""
Hidden Surface Elimination Simulation

This program provides an interactive simulation of hidden surface elimination algorithms:

Features:
1. **Animated Simulation**: Camera rotates around a 3D cube showing real-time 
   hidden surface elimination
2. **Static Views**: Shows 6 different viewing angles with culling results
3. **Visual Feedback**: 
   - Red dot shows camera position
   - Colored faces show visible surfaces
   - Missing faces represent culled (hidden) surfaces
4. **Console Output**: Real-time information about visible/culled surfaces

Algorithms Demonstrated:
- **Back-Face Culling**: Removes faces pointing away from viewer
- **Depth Sorting**: Orders visible faces by distance
- **Real-time Processing**: Updates visibility as camera moves

Educational Value:
- Shows how viewing angle affects surface visibility
- Demonstrates the efficiency of back-face culling
- Visualizes the painter's algorithm for depth sorting

Controls:
- Close window or Ctrl+C to stop simulation
- Animation automatically loops

The simulation helps understand how 3D graphics engines determine
which surfaces to draw for optimal rendering performance.
"""
