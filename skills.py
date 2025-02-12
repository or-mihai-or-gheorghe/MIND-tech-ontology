import os
import json
from typing import Dict, Any, Union, List, Set

# ------------------------------------------------------------------------
# Base Skill Class
# ------------------------------------------------------------------------
class Skill:
    def __init__(
        self,
        name: str,
        synonyms: List[str] = None,
        skill_type: List[str] = None,
        technical_domains: List[str] = None,
        implies_knowing_skills: List[str] = None,
        implies_knowing_concepts: List[str] = None,
        conceptual_aspects: List[str] = None,
        architectural_patterns: List[str] = None,
        **kwargs
    ):
        self.name = name
        self.synonyms = synonyms or []
        self.type = skill_type or []
        self.technicalDomains = technical_domains or []
        self.impliesKnowingSkills = implies_knowing_skills or []
        self.impliesKnowingConcepts = implies_knowing_concepts or []
        self.conceptualAspects = conceptual_aspects or []
        self.architecturalPatterns = architectural_patterns or []

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "name": self.name,
            "synonyms": self.synonyms,
            "type": self.type,
            "technicalDomains": self.technicalDomains,
            "impliesKnowingSkills": self.impliesKnowingSkills,
            "impliesKnowingConcepts": self.impliesKnowingConcepts,
            "conceptualAspects": self.conceptualAspects,
            "architecturalPatterns": self.architecturalPatterns,
        }
        return data

    def merge_from_dict(self, data: Dict[str, Any]):
        if "synonyms" in data:
            self.synonyms = list(set(self.synonyms + data["synonyms"]))
        if "type" in data:
            self.type = list(set(self.type + data["type"]))
        if "technicalDomains" in data:
            self.technicalDomains = list(set(self.technicalDomains + data["technicalDomains"]))
        if "impliesKnowingSkills" in data:
            self.impliesKnowingSkills = list(set(self.impliesKnowingSkills + data["impliesKnowingSkills"]))
        if "impliesKnowingConcepts" in data:
            self.impliesKnowingConcepts = list(set(self.impliesKnowingConcepts + data["impliesKnowingConcepts"]))
        if "conceptualAspects" in data:
            self.conceptualAspects = list(set(self.conceptualAspects + data["conceptualAspects"]))
        if "architecturalPatterns" in data:
            self.architecturalPatterns = list(
                set(self.architecturalPatterns + data["architecturalPatterns"])
            )

# ------------------------------------------------------------------------
# Subclasses
# ------------------------------------------------------------------------
class ProgrammingLanguage(Skill):
    """
    Extends Skill with:
      - buildTools
      - runtimeEnvironments
      - associatedToApplicationDomains
    """

    def __init__(
        self,
        name: str,
        synonyms: List[str] = None,
        skill_type: List[str] = None,
        technical_domains: List[str] = None,
        implies_knowing_skills: List[str] = None,
        implies_knowing_concepts: List[str] = None,
        conceptual_aspects: List[str] = None,
        architectural_patterns: List[str] = None,
        build_tools: List[str] = None,
        runtime_environments: List[str] = None,
        associated_to_app_domains: List[str] = None,
        **kwargs
    ):
        # Ensure type includes ProgrammingLanguage
        if skill_type is None:
            skill_type = ["ProgrammingLanguage"]
        elif "ProgrammingLanguage" not in skill_type:
            skill_type.append("ProgrammingLanguage")
            
        super().__init__(
            name=name,
            synonyms=synonyms,
            skill_type=skill_type,
            technical_domains=technical_domains,
            implies_knowing_skills=implies_knowing_skills,
            implies_knowing_concepts=implies_knowing_concepts,
            conceptual_aspects=conceptual_aspects,
            architectural_patterns=architectural_patterns,
            **kwargs
        )
        self.buildTools = build_tools or []
        self.runtimeEnvironments = runtime_environments or []
        self.associatedToApplicationDomains = associated_to_app_domains or []

    def to_dict(self) -> Dict[str, Any]:
        # Get base class dictionary first
        data = super().to_dict()
        # Add ProgrammingLanguage-specific fields
        data.update({
            "buildTools": self.buildTools,
            "runtimeEnvironments": self.runtimeEnvironments,
            "associatedToApplicationDomains": self.associatedToApplicationDomains,
        })
        return data

    def merge_from_dict(self, data: Dict[str, Any]):
        # Handle base class fields first
        super().merge_from_dict(data)
        
        # Handle ProgrammingLanguage-specific fields
        if "buildTools" in data:
            self.buildTools = list(set(self.buildTools + data["buildTools"]))
        if "runtimeEnvironments" in data:
            self.runtimeEnvironments = list(set(self.runtimeEnvironments + data["runtimeEnvironments"]))
        if "associatedToApplicationDomains" in data:
            self.associatedToApplicationDomains = list(
                set(self.associatedToApplicationDomains + data["associatedToApplicationDomains"])
            )

class QueryLanguage(Skill):
    """
    Minimal QueryLanguage subclass—no extra fields beyond the base Skill.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self) -> Dict[str, Any]:
        return super().to_dict()

    def merge_from_dict(self, data: Dict[str, Any]):
        super().merge_from_dict(data)


class ScriptingLanguage(Skill):
    """
    Minimal ScriptingLanguage subclass—no extra fields beyond the base Skill.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self) -> Dict[str, Any]:
        return super().to_dict()

    def merge_from_dict(self, data: Dict[str, Any]):
        super().merge_from_dict(data)


class MarkupLanguage(Skill):
    """
    Minimal MarkupLanguage subclass—no extra fields beyond the base Skill.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self) -> Dict[str, Any]:
        return super().to_dict()

    def merge_from_dict(self, data: Dict[str, Any]):
        super().merge_from_dict(data)


class Framework(Skill):
    """
    Extends Skill with:
      - implementsPatternsByDefault
      - implementsPatternsThroughLibrariesAndServices
      - associatedToApplicationDomains
      - solvesApplicationTasks
    """
    def __init__(
        self,
        name: str,
        synonyms: List[str] = None,
        skill_type: List[str] = None,
        technical_domains: List[str] = None,
        implies_knowing_skills: List[str] = None,
        implies_knowing_concepts: List[str] = None,
        conceptual_aspects: List[str] = None,
        implements_patterns_by_default: List[str] = None,
        implements_patterns_through_libs: List[str] = None,
        associated_to_app_domains: List[str] = None,
        solves_app_tasks: List[str] = None,
        **kwargs
    ):
        super().__init__(
            name=name,
            synonyms=synonyms,
            skill_type=skill_type,
            technical_domains=technical_domains,
            implies_knowing_skills=implies_knowing_skills,
            implies_knowing_concepts=implies_knowing_concepts,
            conceptual_aspects=conceptual_aspects,
            **kwargs
        )
        self.implementsPatternsByDefault = implements_patterns_by_default or []
        self.implementsPatternsThroughLibrariesAndServices = implements_patterns_through_libs or []
        self.associatedToApplicationDomains = associated_to_app_domains or []
        self.solvesApplicationTasks = solves_app_tasks or []

    def to_dict(self) -> Dict[str, Any]:
        base = super().to_dict()
        base.update({
            "implementsPatternsByDefault": self.implementsPatternsByDefault,
            "implementsPatternsThroughLibrariesAndServices": self.implementsPatternsThroughLibrariesAndServices,
            "associatedToApplicationDomains": self.associatedToApplicationDomains,
            "solvesApplicationTasks": self.solvesApplicationTasks,
        })
        return base

    def merge_from_dict(self, data: Dict[str, Any]):
        super().merge_from_dict(data)

        if "implementsPatternsByDefault" in data:
            self.implementsPatternsByDefault = list(
                set(self.implementsPatternsByDefault + data["implementsPatternsByDefault"])
            )
        if "implementsPatternsThroughLibrariesAndServices" in data:
            self.implementsPatternsThroughLibrariesAndServices = list(
                set(self.implementsPatternsThroughLibrariesAndServices
                    + data["implementsPatternsThroughLibrariesAndServices"])
            )
        if "associatedToApplicationDomains" in data:
            self.associatedToApplicationDomains = list(
                set(self.associatedToApplicationDomains + data["associatedToApplicationDomains"])
            )
        if "solvesApplicationTasks" in data:
            self.solvesApplicationTasks = list(
                set(self.solvesApplicationTasks + data["solvesApplicationTasks"])
            )

class Library(Skill):
    """
    Extends Skill with:
      - supportedProgrammingLanguages
      - specificToFrameworks
      - adapterForToolOrService
      - implementsPatterns
      - associatedToApplicationDomains
      - solvesApplicationTasks
    """
    def __init__(
        self,
        name: str,
        synonyms: List[str] = None,
        skill_type: List[str] = None,
        technical_domains: List[str] = None,
        implies_knowing_skills: List[str] = None,
        implies_knowing_concepts: List[str] = None,
        conceptual_aspects: List[str] = None,
        supported_programming_languages: List[str] = None,
        specific_to_frameworks: List[str] = None,
        adapter_for_tool_or_service: List[str] = None,
        implements_patterns: List[str] = None,
        associated_to_app_domains: List[str] = None,
        solves_app_tasks: List[str] = None,
        **kwargs
    ):
        super().__init__(
            name=name,
            synonyms=synonyms,
            skill_type=skill_type,
            technical_domains=technical_domains,
            implies_knowing_skills=implies_knowing_skills,
            implies_knowing_concepts=implies_knowing_concepts,
            conceptual_aspects=conceptual_aspects,
            **kwargs
        )
        self.supportedProgrammingLanguages = supported_programming_languages or []
        self.specificToFrameworks = specific_to_frameworks or []
        self.adapterForToolOrService = adapter_for_tool_or_service or []
        self.implementsPatterns = implements_patterns or []
        self.associatedToApplicationDomains = associated_to_app_domains or []
        self.solvesApplicationTasks = solves_app_tasks or []

    def to_dict(self) -> Dict[str, Any]:
        base = super().to_dict()
        base.update({
            "supportedProgrammingLanguages": self.supportedProgrammingLanguages,
            "specificToFrameworks": self.specificToFrameworks,
            "adapterForToolOrService": self.adapterForToolOrService,
            "implementsPatterns": self.implementsPatterns,
            "associatedToApplicationDomains": self.associatedToApplicationDomains,
            "solvesApplicationTasks": self.solvesApplicationTasks,
        })
        return base

    def merge_from_dict(self, data: Dict[str, Any]):
        super().merge_from_dict(data)

        if "supportedProgrammingLanguages" in data:
            self.supportedProgrammingLanguages = list(
                set(self.supportedProgrammingLanguages + data["supportedProgrammingLanguages"])
            )
        if "specificToFrameworks" in data:
            self.specificToFrameworks = list(
                set(self.specificToFrameworks + data["specificToFrameworks"])
            )
        if "adapterForToolOrService" in data:
            self.adapterForToolOrService = list(
                set(self.adapterForToolOrService + data["adapterForToolOrService"])
            )
        if "implementsPatterns" in data:
            self.implementsPatterns = list(
                set(self.implementsPatterns + data["implementsPatterns"])
            )
        if "associatedToApplicationDomains" in data:
            self.associatedToApplicationDomains = list(
                set(self.associatedToApplicationDomains + data["associatedToApplicationDomains"])
            )
        if "solvesApplicationTasks" in data:
            self.solvesApplicationTasks = list(
                set(self.solvesApplicationTasks + data["solvesApplicationTasks"])
            )

class Database(Skill):
    """
    Extends Skill to represent a Database technology, with specific properties:
      - deploymentType: [on-premise, cloud, as a Service]
      - integrationTools: List of Skill names for integration tools/connectors
      - parentCompany: Parent company or product group (e.g., Oracle, AWS, GCP).
                       This is a free-form text field and is NOT validated against a list.
    """
    def __init__(
        self,
        name: str,
        synonyms: List[str] = None,
        skill_type: List[str] = None,
        technical_domains: List[str] = None,
        implies_knowing_skills: List[str] = None,
        implies_knowing_concepts: List[str] = None,
        conceptual_aspects: List[str] = None,
        architectural_patterns: List[str] = None,
        deployment_type: List[str] = None,
        integration_tools: List[str] = None, # List of Skill names (strings)
        parent_company: str = None,
        **kwargs
    ):
        # Ensure type includes Database
        if skill_type is None:
            skill_type = ["Database"]
        elif "Database" not in skill_type:
            skill_type.append("Database")

        super().__init__(
            name=name,
            synonyms=synonyms,
            skill_type=skill_type,
            technical_domains=technical_domains,
            implies_knowing_skills=implies_knowing_skills,
            implies_knowing_concepts=implies_knowing_concepts,
            conceptual_aspects=conceptual_aspects,
            architectural_patterns=architectural_patterns,
            **kwargs
        )
        self.deploymentType = deployment_type or []
        self.integrationTools = integration_tools or [] # List of Skill names (strings)
        self.parentCompany = parent_company

    def to_dict(self) -> Dict[str, Any]:
        # Get base class dictionary first
        data = super().to_dict()
        # Add Database-specific fields
        data.update({
            "deploymentType": self.deploymentType,
            "integrationTools": self.integrationTools,
            "parentCompany": self.parentCompany,
        })
        return data

    def merge_from_dict(self, data: Dict[str, Any]):
        # Handle base class fields first
        super().merge_from_dict(data)

        # Handle Database-specific fields
        if "deploymentType" in data:
            self.deploymentType = list(set(self.deploymentType + data["deploymentType"]))
        if "integrationTools" in data:
            self.integrationTools = list(set(self.integrationTools + data["integrationTools"]))
        if "parentCompany" in data:
            self.parentCompany = data["parentCompany"] # For parentCompany, last value wins in merge

class Tool(Skill):
    """
    Represents a tech tool that can be installed locally (as an app or CLI tool).
    Tools may be available in various deployment types (e.g. on-premise, cloud,
    or as a Service) and are distinct from libraries or frameworks.
    They can optionally be associated with one or more application domains and/or
    solve one or more application tasks.
    """
    def __init__(
        self,
        name: str,
        synonyms: List[str] = None,
        skill_type: List[str] = None,
        technical_domains: List[str] = None,
        implies_knowing_skills: List[str] = None,
        implies_knowing_concepts: List[str] = None,
        conceptual_aspects: List[str] = None,
        architectural_patterns: List[str] = None,
        deployment_type: List[str] = None,
        associated_to_app_domains: List[str] = None,
        solves_app_tasks: List[str] = None,
        **kwargs
    ):
        # Ensure the skill_type includes "Tool"
        if skill_type is None:
            skill_type = ["Tool"]
        elif "Tool" not in skill_type:
            skill_type.append("Tool")
            
        super().__init__(
            name=name,
            synonyms=synonyms,
            skill_type=skill_type,
            technical_domains=technical_domains,
            implies_knowing_skills=implies_knowing_skills,
            implies_knowing_concepts=implies_knowing_concepts,
            conceptual_aspects=conceptual_aspects,
            architectural_patterns=architectural_patterns,
            **kwargs
        )
        self.deploymentType = deployment_type or []
        self.associatedToApplicationDomains = associated_to_app_domains or []
        self.solvesApplicationTasks = solves_app_tasks or []

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "deploymentType": self.deploymentType,
            "associatedToApplicationDomains": self.associatedToApplicationDomains,
            "solvesApplicationTasks": self.solvesApplicationTasks,
        })
        return data

    def merge_from_dict(self, data: Dict[str, Any]):
        super().merge_from_dict(data)
        if "deploymentType" in data:
            self.deploymentType = list(set(self.deploymentType + data["deploymentType"]))
        if "associatedToApplicationDomains" in data:
            self.associatedToApplicationDomains = list(
                set(self.associatedToApplicationDomains + data["associatedToApplicationDomains"])
            )
        if "solvesApplicationTasks" in data:
            self.solvesApplicationTasks = list(
                set(self.solvesApplicationTasks + data["solvesApplicationTasks"])
            )

class Service(Skill):
    """
    Represents a tech service/platform/API.
    Extends Skill with:
      - groups: a list of technology groups or companies that the service is part of (e.g. AWS, SAP, Open AI)
      - deploymentType: deployment methods (e.g. on-premise, cloud, SaaS)
      - solvesApplicationTasks: application tasks the service addresses
      - associatedToApplicationDomains: application domains related to the service
    """
    def __init__(
        self,
        name: str,
        synonyms: List[str] = None,
        skill_type: List[str] = None,
        technical_domains: List[str] = None,
        implies_knowing_skills: List[str] = None,
        implies_knowing_concepts: List[str] = None,
        conceptual_aspects: List[str] = None,
        architectural_patterns: List[str] = None,
        groups: List[str] = None,
        deployment_type: List[str] = None,
        solves_app_tasks: List[str] = None,
        associated_to_app_domains: List[str] = None,
        **kwargs
    ):
        # Ensure the skill type includes "Service"
        if skill_type is None:
            skill_type = ["Service"]
        elif "Service" not in skill_type:
            skill_type.append("Service")
            
        super().__init__(
            name=name,
            synonyms=synonyms,
            skill_type=skill_type,
            technical_domains=technical_domains,
            implies_knowing_skills=implies_knowing_skills,
            implies_knowing_concepts=implies_knowing_concepts,
            conceptual_aspects=conceptual_aspects,
            architectural_patterns=architectural_patterns,
            **kwargs
        )
        self.groups = groups or []
        self.deploymentType = deployment_type or []
        self.solvesApplicationTasks = solves_app_tasks or []
        self.associatedToApplicationDomains = associated_to_app_domains or []

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "groups": self.groups,
            "deploymentType": self.deploymentType,
            "solvesApplicationTasks": self.solvesApplicationTasks,
            "associatedToApplicationDomains": self.associatedToApplicationDomains,
        })
        return data

    def merge_from_dict(self, data: Dict[str, Any]):
        super().merge_from_dict(data)
        if "groups" in data:
            self.groups = list(set(self.groups + data["groups"]))
        if "deploymentType" in data:
            self.deploymentType = list(set(self.deploymentType + data["deploymentType"]))
        if "solvesApplicationTasks" in data:
            self.solvesApplicationTasks = list(set(self.solvesApplicationTasks + data["solvesApplicationTasks"]))
        if "associatedToApplicationDomains" in data:
            self.associatedToApplicationDomains = list(set(self.associatedToApplicationDomains + data["associatedToApplicationDomains"]))


# ------------------------------------------------------------------------
# Taxonomy Class
# ------------------------------------------------------------------------
import json
import os
from typing import Dict, Any, Union, List, Set

class Taxonomy:
    """
    Updated Taxonomy class that:
      - Stores skill names and synonyms in a case-insensitive manner (in _skills and _synonyms_map).
      - Allows loading enumerations (concepts) from separate JSON files so new skills
        can only reference domains/tasks/patterns that exist in those enumerations.
      - For conceptualAspects that are not in the allowed set, we prefix them with '__'
        instead of throwing an error.
    """

    def __init__(self):
        # key: lowercase skill name, value: Skill object
        self._skills: Dict[str, Skill] = {}
        # key: lowercase synonym, value: lowercase canonical name
        self._synonyms_map: Dict[str, str] = {}

        # Allowed enumerations loaded from concepts
        self._allowed_technical_domains: Set[str] = set()
        self._allowed_vertical_domains: Set[str] = set()
        self._allowed_application_domains: Set[str] = set()
        self._allowed_application_tasks: Set[str] = set()
        self._allowed_architectural_patterns: Set[str] = set()
        self._allowed_conceptual_aspects: Set[str] = set()
        self._allowed_deployment_types: Set[str] = set()

    def load_concepts(self, concepts_folder: str):
        """
        Load enumerations from JSON files in 'concepts_folder'.
        Each JSON file is expected to have a known structure
        (simple list or category-based).
        """
        # technical_domains.json
        td_path = os.path.join(concepts_folder, "technical_domains.json")
        if os.path.isfile(td_path):
            self._allowed_technical_domains = self._load_simple_list(td_path)

        # vertical_domains.json
        vd_path = os.path.join(concepts_folder, "vertical_domains.json")
        if os.path.isfile(vd_path):
            self._allowed_vertical_domains = self._load_simple_list(vd_path)

        # application_domains.json
        ad_path = os.path.join(concepts_folder, "application_domains.json")
        if os.path.isfile(ad_path):
            self._allowed_application_domains = self._load_list_or_category_based(ad_path, list_key=None)

        # application_tasks.json
        at_path = os.path.join(concepts_folder, "application_tasks.json")
        if os.path.isfile(at_path):
            self._allowed_application_tasks = self._load_list_or_category_based(at_path, list_key=None)

        # architectural_patterns.json
        ap_path = os.path.join(concepts_folder, "architectural_patterns.json")
        if os.path.isfile(ap_path):
            self._allowed_architectural_patterns = self._load_arch_patterns(ap_path)

        # conceptual_aspects.json
        ca_path = os.path.join(concepts_folder, "conceptual_aspects.json")
        if os.path.isfile(ca_path):
            self._allowed_conceptual_aspects = self._load_list_or_category_based(ca_path, list_key=None)

        # skill_deployment_types.json
        ddt_path = os.path.join(concepts_folder, "skill_deployment_types.json")
        if os.path.isfile(ddt_path):
            self._allowed_deployment_types = self._load_simple_list(ddt_path)

    def _load_simple_list(self, file_path: str) -> Set[str]:
        """
        For JSON files with a simple array of strings, e.g. ["Backend","Frontend"].
        """
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list) and all(isinstance(x, str) for x in data):
            return set(data)
        return set()

    def _load_arch_patterns(self, file_path: str) -> Set[str]:
        """
        For 'architectural_patterns.json', often an array like:
          [ { "category": "...", "patterns": ["...", "..."] }, ... ]
        Flatten to a set of pattern names.
        """
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            return set()

        patterns = set()
        for block in data:
            if isinstance(block, dict):
                pat_list = block.get("patterns", [])
                for p in pat_list:
                    patterns.add(p)
        return patterns

    def _load_list_or_category_based(self, file_path: str, list_key: str = None) -> Set[str]:
        """
        For JSON that might be a simple list of strings or a list of category-based dicts.
        If 'list_key' is provided, we look for dict[list_key].
        If not, we attempt to flatten all string arrays found in each dict block.
        """
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        results = set()
        if isinstance(data, list):
            # If the file is a direct list of strings
            if data and all(isinstance(x, str) for x in data):
                results = set(data)
            # Possibly list of dicts with categories
            elif data and isinstance(data[0], dict):
                for block in data:
                    if isinstance(block, dict):
                        if list_key and block.get(list_key):
                            for item in block[list_key]:
                                results.add(item)
                        else:
                            # Flatten from any list found in the block
                            for val in block.values():
                                if isinstance(val, list):
                                    for item in val:
                                        if isinstance(item, str):
                                            results.add(item)
        return results

    def _validate_domains_and_concepts(self, data: Dict[str, Any]):
            """
            Validate each domain/idea against the allowed sets. If a conceptual aspect
            is NOT in the allowed set, prefix it with '__' for later manual review instead
            of raising an error.
            """
            # Validate technical domains
            if "technicalDomains" in data:
                for td in data["technicalDomains"]:
                    if td not in self._allowed_technical_domains:
                        raise ValueError(f"Invalid technical domain: {td}")

            # Validate vertical domains
            if "verticalDomains" in data:
                for vd in data["verticalDomains"]:
                    if vd not in self._allowed_vertical_domains:
                        raise ValueError(f"Invalid vertical domain: {vd}")

            # Validate application domains - critical fix here
            if "associatedToApplicationDomains" in data:
                # Only validate if the domains set is loaded
                if self._allowed_application_domains:
                    for ad in data["associatedToApplicationDomains"]:
                        if ad not in self._allowed_application_domains:
                            raise ValueError(f"Invalid application domain: {ad}")

            # Validate application tasks
            if "solvesApplicationTasks" in data:
                for st in data["solvesApplicationTasks"]:
                    if st not in self._allowed_application_tasks:
                        raise ValueError(f"Invalid application task: {st}")

            # Handle conceptual aspects with prefix for unknown ones
            if "conceptualAspects" in data:
                updated_aspects = []
                for ca in data["conceptualAspects"]:
                    if ca.lower() not in (x.lower() for x in self._allowed_conceptual_aspects):
                        if not ca.startswith("__"):
                            updated_aspects.append(f"__{ca}")
                        else:
                            updated_aspects.append(ca)
                    else:
                        updated_aspects.append(ca)
                data["conceptualAspects"] = updated_aspects

            # Validate architectural patterns
            if "architecturalPatterns" in data:
                for ap in data["architecturalPatterns"]:
                    if ap not in self._allowed_architectural_patterns:
                        raise ValueError(f"Invalid architectural pattern: {ap}")

            # Validate deployment types (case-insensitive)
            if "deploymentType" in data:
                for dt in data["deploymentType"]:
                    if dt.lower() not in (allowed_dt.lower() for allowed_dt in self._allowed_deployment_types):
                        raise ValueError(f"Invalid deployment type: {dt}")

            return data  # Return validated data

    def _create_skill_instance(self, data: Dict[str, Any]) -> Skill:
        constructor_args = {
            "name": data["name"],
            "synonyms": data.get("synonyms", []),
            "skill_type": data.get("type", []),
            "technical_domains": data.get("technicalDomains", []),
            "implies_knowing_skills": data.get("impliesKnowingSkills", []),
            "implies_knowing_concepts": data.get("impliesKnowingConcepts", []),
            "conceptual_aspects": data.get("conceptualAspects", []),
            "architectural_patterns": data.get("architecturalPatterns", []),
            # Make sure ProgrammingLanguage gets the application domains
            "associated_to_app_domains": data.get("associatedToApplicationDomains", []),
            # Other existing fields
            "build_tools": data.get("buildTools", []),
            "runtime_environments": data.get("runtimeEnvironments", []),
            "implements_patterns_by_default": data.get("implementsPatternsByDefault", []),
            "implements_patterns_through_libs": data.get("implementsPatternsThroughLibrariesAndServices", []),
            "solves_app_tasks": data.get("solvesApplicationTasks", []),
            "supported_programming_languages": data.get("supportedProgrammingLanguages", []),
            "specific_to_frameworks": data.get("specific_to_frameworks", []),
            "adapter_for_tool_or_service": data.get("adapterForToolOrService", []),
            "implements_patterns": data.get("implementsPatterns", []),
            # Database specific args (also used in the heuristic)
            "deployment_type": data.get("deploymentType", []),
            "integration_tools": data.get("integrationTools", []),
            "parent_company": data.get("parentCompany", None),
            "groups": data.get("groups", []),
        }

        recognized_types_map = {
            "ProgrammingLanguage": ProgrammingLanguage,
            "QueryLanguage": QueryLanguage,
            "ScriptingLanguage": ScriptingLanguage,
            "MarkupLanguage": MarkupLanguage,
            "Framework": Framework,
            "Library": Library,
            "Database": Database,
            "Tool": Tool,
            "Service": Service,
        }

        # Existing heuristics for type determination (if not explicitly set)
        if not data.get("type") and (data.get("buildTools") or data.get("runtimeEnvironments")):
            constructor_args["skill_type"] = ["ProgrammingLanguage"]
        if not data.get("type") and (data.get("deploymentType") or data.get("parentCompany")):
            constructor_args["skill_type"] = ["Database"]

        skill_class = Skill
        # Pick the first recognized type if multiple are listed
        for t in constructor_args["skill_type"]:
            if t in recognized_types_map:
                skill_class = recognized_types_map[t]
                break

        return skill_class(**constructor_args)

    def add_skill_from_dict(self, data: Dict[str, Any]):
        """
        Add or merge a skill definition from a dict in a case-insensitive way.
        - If the skill (name or synonym) already exists, we merge.
        - Otherwise, we create a new instance.
        - We also validate references to enumerations before creation/merge.
        """
        if "name" not in data or not data["name"]:
            return

        # Validate references
        self._validate_domains_and_concepts(data)

        skill_name_original = data["name"]
        skill_name_key = skill_name_original.lower()

        # 1. Attempt to find an existing skill by lowercase name
        existing_skill = self.get_skill(skill_name_key)
        if not existing_skill:
            # 2. If not found, see if the name is in synonyms_map
            if skill_name_key in self._synonyms_map:
                canonical = self._synonyms_map[skill_name_key]
                existing_skill = self._skills.get(canonical)

        # 3. If there's still no existing skill, create new
        if not existing_skill:
            new_skill = self._create_skill_instance(data)
            self._skills[skill_name_key] = new_skill
            # Register synonyms
            for syn in new_skill.synonyms:
                self._synonyms_map[syn.lower()] = skill_name_key
        else:
            # Merge data into existing skill
            existing_skill.merge_from_dict(data)
            # Merge synonyms
            new_syns = data.get("synonyms", [])
            for syn in new_syns:
                self._synonyms_map[syn.lower()] = self._find_canonical_key_for_skill(existing_skill)

    def get_skill(self, name_or_synonym: str) -> Union[Skill, None]:
        """
        Look up a Skill by exact name or known synonym (case-insensitive).
        Returns None if not found.
        """
        if not name_or_synonym:
            return None

        key = name_or_synonym.lower()
        if key in self._skills:
            return self._skills[key]
        if key in self._synonyms_map:
            canonical = self._synonyms_map[key]
            return self._skills.get(canonical)
        return None

    def add_property(self, skill_name: str, property_name: str, value: Any):
        """
        Append or overwrite a property on an existing skill (case-insensitive name).
        If it's a list property, we do a union merge.
        """
        skill = self.get_skill(skill_name)
        if not skill:
            return

        existing_val = getattr(skill, property_name, None)
        if isinstance(existing_val, list):
            if isinstance(value, list):
                merged = list(set(existing_val + value))
            else:
                merged = list(set(existing_val + [value]))
            setattr(skill, property_name, merged)
        else:
            setattr(skill, property_name, value)

    def _find_canonical_key_for_skill(self, skill_obj: Skill) -> str:
        """
        Return the lowercase key in _skills that maps to skill_obj.
        """
        for k, v in self._skills.items():
            if v is skill_obj:
                return k
        return ""

    def import_from_json(self, file_path: str):
        """
        Import from a JSON array of skill dicts or a dict of name->skill dict.
        """
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    self.add_skill_from_dict(item)
        elif isinstance(data, dict):
            for _, skill_def in data.items():
                if isinstance(skill_def, dict):
                    self.add_skill_from_dict(skill_def)

    def export_to_json(self, file_path: str):
        """
        Export all skills as a JSON array of dicts.
        """
        skill_list = []
        for skill_obj in self._skills.values():
            skill_list.append(skill_obj.to_dict())
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(skill_list, f, indent=4)

    @staticmethod
    def get_all_frameworks_for_skill(skill_name: str):
        found_frameworks = []

        frameworks_backend_path = 'skills/frameworks_backend.json'
        frameworks_frontend_path = 'skills/frameworks_frontend.json'
        frameworks_mobile_path = 'skills/frameworks_mobile.json'

        frameworks_backend = None
        with open(frameworks_backend_path, "r", encoding="utf-8") as f:
            frameworks_backend = json.load(f)

        frameworks_frontend = None
        with open(frameworks_frontend_path, "r", encoding="utf-8") as f:
            frameworks_frontend = json.load(f)

        frameworks_mobile = None
        with open(frameworks_mobile_path, "r", encoding="utf-8") as f:
            frameworks_mobile = json.load(f)

        for framework_type in [frameworks_mobile, frameworks_backend, frameworks_frontend]:
            for obj in framework_type:
                if skill_name in obj['impliesKnowingSkills']:
                    found_frameworks.append(obj['name'])

        return found_frameworks
