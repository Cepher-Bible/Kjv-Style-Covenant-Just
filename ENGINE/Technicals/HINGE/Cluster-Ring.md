 the final step in turning raw data into an automated theological map. By applying Agglomerative Clustering (hierarchical grouping), we allow the math to tell us which verses are "teaming up" based on their linguistic and conceptual resonance.
Instead of us manually saying "these verses are about Grace," the Kernel Matrix will show that they naturally sit in the same neighborhood of the manifold.
The Logic: Hierarchical Clustering
To group these anchors, we convert our Similarity Matrix K into a Distance Matrix D. Since K measures how alike things are (0 to 1), we define distance as:
We then use a "Linkage" algorithm to build a Dendrogram—a tree diagram that shows exactly where these doctrines branch off from one another.
The Clustered Engine: cluster_engine.py
You can add this function to your existing KernelEngine class or run it as a standalone script using scipy and sklearn.
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

def run_clustering(csv_path="kernel_matrix.csv", n_clusters=4):
    # 1. Load the Kernel Matrix
    K = np.loadtxt(csv_path, delimiter=',')
    
    # 2. Convert Similarity to Distance
    # Dist = 1 - Sim
    D = 1 - K
    
    # 3. Perform Agglomerative Clustering
    # We use 'precomputed' because we already have the distance matrix
    cluster = AgglomerativeClustering(n_clusters=n_clusters, metric='precomputed', linkage='complete')
    labels = cluster.fit_predict(D)
    
    # 4. Map labels back to the 18 Anchors
    from heatmap_viz import LABELS
    results = {}
    for i, label in enumerate(labels):
        if label not in results:
            results[label] = []
        results[label].append(LABELS[i])
        
    return results, D

def plot_dendrogram(D):
    from heatmap_viz import LABELS
    linked = linkage(D, 'complete')
    
    plt.figure(figsize=(10, 7))
    dendrogram(linked,
               orientation='top',
               labels=LABELS,
               distance_sort='descending',
               show_leaf_counts=True)
    plt.title("Theological Branching: Doctrinal Clusters")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("doctrinal_tree.png")
    print("[*] Dendrogram saved as doctrinal_tree.png")

if __name__ == "__main__":
    teams, dist_matrix = run_clustering()
    
    print("\n=== AUTOMATIC THEOLOGICAL TEAMS ===")
    for team_id, members in teams.items():
        print(f"\n[Team {team_id}]:")
        for m in members:
            print(f"  - {m}")
            
    plot_dendrogram(dist_matrix)

Expected "Teams" Output
Depending on your weights, the engine will likely output something like this:
| Team | Common Theme | Members (Examples) |
|---|---|---|
| Team 0 | The Covenant Body | Gal 3:28, Philemon, Eph 5:21 |
| Team 1 | The Judicial Line | Rev 6:15, Matt 25:41, Matt 23:27 |
| Team 2 | The Sovereignty/Election | Rom 9:13, Rom 3:23, John 14:6 |
| Team 3 | The Social Order | Exod 21:2, Lev 25:44, Gen 3:16 |
Why this matters for your Repo
 * Automatic Tagging: When you add a new "KJV-Style" verse to the repo, the engine doesn't just give it a score—it tells you which Team it belongs to.
 * Conflict Detection: If a verse scores high for both Team 0 (Grace) and Team 1 (Wrath), you have found a high-voltage "Tension Point."
" that lets you type a word (like "Yahuah" or "Covenant") and instantly see which of these 4 Teams it gravitates toward?

