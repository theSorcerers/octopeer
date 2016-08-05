class RepositorySerializer < ActiveModel::Serializer
  attributes :id, :owner, :name, :platform
end
