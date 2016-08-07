class SemanticEvent < ApplicationRecord
  belongs_to :session
  belongs_to :event_type
  belongs_to :element_type
end
