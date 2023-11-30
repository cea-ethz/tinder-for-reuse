import React, { useEffect, useState } from "react";
import {
  BuildingElementCard,
  BuildingElementCardSkeleton,
} from "../BuildingElementCard";
import { CollectorCard, CollectorCardSkeleton } from "../CollectorCard";
import CollectorsMap from "../CollectorsMap";
import { CollectorRead } from "@/types/api/collector";

export type ResultsWrapperType = {
  results: any[];
  isLoading: boolean;
};

export function BuildingElementResultsWrapper({
  results,
  isLoading,
}: ResultsWrapperType) {
  return (
    <>
      {results.map((result, index) => (
        <BuildingElementCard key={index} {...result} />
      ))}
      {isLoading && (
        <>
          <BuildingElementCardSkeleton />
          <BuildingElementCardSkeleton />
          <BuildingElementCardSkeleton />
        </>
      )}
    </>
  );
}

export function CollectorResultsWrapper({
  results,
  isLoading,
}: ResultsWrapperType) {
  const collectors = results as CollectorRead[];
  const [visibleCollectorIds, setVisibleCollectorIds] = useState<number[]>([]);
  const [activeCollector, setActiveCollector] = useState<CollectorRead | null>(
    null
  );
  const IGNORE_DEACTIVATION_CLASS = "ignore-deactivation";

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      const target = event.target as Element;
      // only deactivate if the click is outside the active collector
      if (!target.closest(`.${IGNORE_DEACTIVATION_CLASS}`)) {
        setActiveCollector(null);
      }
    };
    document.addEventListener("click", handleClickOutside);

    return () => {
      document.removeEventListener("click", handleClickOutside);
    };
  }, []);

  useEffect(() => {
    setVisibleCollectorIds(collectors.map((collector) => collector.id));
  }, [collectors]);

  return (
    <>
      <CollectorsMap
        collectors={collectors}
        activeCollector={activeCollector}
        setActiveCollector={setActiveCollector}
        setVisibleCollectorIds={setVisibleCollectorIds}
        className={IGNORE_DEACTIVATION_CLASS}
      />
      {collectors
        .filter((collector) => visibleCollectorIds.includes(collector.id))
        .map((visibleCollector, index) => (
          <a
            onClick={() => setActiveCollector(visibleCollector)}
            key={index}
            className={`cursor-pointer ${IGNORE_DEACTIVATION_CLASS}`}
          >
            <CollectorCard
              {...visibleCollector}
              isActive={activeCollector?.id === visibleCollector.id}
            />
          </a>
        ))}
      {isLoading && (
        <>
          <CollectorCardSkeleton />
          <CollectorCardSkeleton />
          <CollectorCardSkeleton />
        </>
      )}
    </>
  );
}