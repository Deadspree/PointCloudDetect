import open3d as o3d

def visualize_ply(file_path):
    # Load the point cloud
    point_cloud = o3d.io.read_point_cloud(file_path)

    if point_cloud.is_empty():
        raise RuntimeError("Loaded point cloud is empty. Check the input file.")

    # Visualize the point cloud
    print("Displaying point cloud. Close the visualization window to exit.")
    o3d.visualization.draw_geometries([point_cloud])

if __name__ == "__main__":
    ply_file = "cleaned_bottle.ply"  # Replace with your PLY file path
    visualize_ply(ply_file)
