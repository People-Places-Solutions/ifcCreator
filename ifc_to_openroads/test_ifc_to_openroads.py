import extractor
import config
ifc_in = r"ifc_to_openroads\data\ifc_data.ifc"

dfs = extractor.get_property_sets(
    in_file=ifc_in
)
for item_type, df in dfs.items():
    df.to_csv(f"ifc_to_openroads\data\{item_type}.csv", index=False)
